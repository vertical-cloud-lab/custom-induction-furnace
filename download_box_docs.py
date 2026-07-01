#!/usr/bin/env python3
"""
Script to download documentation from a Box shared folder.

This script downloads every file from the Box shared link, including files
nested inside subfolders, preserving the folder structure:
https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

The files are saved (by default) to the `docs/` directory.

Usage:
    python download_box_docs.py [--output-dir docs] [--max-bytes N]

The script crawls the shared folder (and all of its subfolders) to discover
every file, then downloads each one using Box's web download endpoint.
"""

import sys
import argparse
import re
import html
from pathlib import Path

try:
    import requests
except ImportError:
    print("❌ 'requests' package is required. Install with: pip install requests")
    sys.exit(1)


SHARED_TOKEN = "lh04mmpkhvhy4vtokpm4sol711xycrph"
SHARED_LINK = f"https://byu.box.com/s/{SHARED_TOKEN}"
ROOT_FOLDER_ID = "87111449214"

# GitHub rejects any single file larger than 100 MiB on push, so by default we
# skip files above this size. Override with --max-bytes 0 to download them all.
DEFAULT_MAX_BYTES = 100 * 1024 * 1024


def _extract_token(shared_link: str) -> str:
    """Accept a full Box shared link or a bare token and return the token."""
    m = re.search(r"/s/([A-Za-z0-9]+)", shared_link)
    return m.group(1) if m else shared_link.strip()


def _new_session() -> "requests.Session":
    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
        }
    )
    return session


def _discover_root_folder_id(session: "requests.Session", token: str) -> str:
    """Read the shared link landing page and extract its root folder id."""
    r = session.get(f"https://byu.box.com/s/{token}", timeout=60)
    r.raise_for_status()
    m = re.search(r'"currentFolderID":"?(\d+)', r.text)
    if not m:
        raise RuntimeError(f"Could not discover root folder id for token {token}")
    return m.group(1)


def _folder_page(session: "requests.Session", folder_id: str, token: str) -> str:
    """Fetch the server-rendered HTML page for a folder in the shared link."""
    url = f"https://byu.box.com/s/{token}/folder/{folder_id}"
    r = session.get(url, timeout=60)
    r.raise_for_status()
    return r.text


def _parse_items(content: str) -> list[dict]:
    """
    Parse a folder page's embedded JSON for its direct children.

    Each item appears as:
        "typedID":"f_<id>" or "d_<id>" ... "name":"<name>" ... "itemSize":<n>

    Returns a list of dicts with keys: type ('file'/'folder'), id, name, size.
    """
    items = []
    pattern = re.compile(
        r'"typedID":"([df])_(\d+)".*?"name":"([^"]+)"(.*?)(?="typedID"|$)',
        re.DOTALL,
    )
    for match in pattern.finditer(content):
        type_char, item_id, raw_name, rest = match.groups()
        size_match = re.search(r'"itemSize":(\d+)', rest)
        name = html.unescape(raw_name.encode().decode("unicode_escape"))
        items.append(
            {
                "type": "folder" if type_char == "d" else "file",
                "id": item_id,
                "name": name,
                "size": int(size_match.group(1)) if size_match else None,
            }
        )
    return items


def discover_files(
    session: "requests.Session", token: str, root_folder_id: str
) -> list[dict]:
    """
    Recursively crawl the shared folder and all subfolders.

    Returns a list of dicts with keys: id, name, size, path (relative path
    including subfolders).
    """
    files: list[dict] = []
    visited: set[str] = set()

    def walk(folder_id: str, rel_path: str) -> None:
        if folder_id in visited:
            return
        visited.add(folder_id)

        try:
            content = _folder_page(session, folder_id, token)
        except Exception as e:  # noqa: BLE001 - report and continue crawling
            print(f"  ✗ Failed to list folder {rel_path or '/'}: {e}")
            return

        for item in _parse_items(content):
            child_path = f"{rel_path}/{item['name']}" if rel_path else item["name"]
            if item["type"] == "folder":
                walk(item["id"], child_path)
            else:
                files.append(
                    {
                        "id": item["id"],
                        "name": item["name"],
                        "size": item["size"],
                        "path": child_path,
                    }
                )

    walk(root_folder_id, "")
    return files


def download_file(
    session: "requests.Session",
    file_id: str,
    output_path: Path,
    token: str,
) -> bool:
    """
    Download a single file from the Box shared folder.

    Returns True if the download succeeded, False otherwise.
    """
    download_url = (
        f"https://byu.app.box.com/index.php"
        f"?rm=box_download_shared_file"
        f"&shared_name={token}"
        f"&file_id=f_{file_id}"
    )

    try:
        r = session.get(download_url, timeout=300, allow_redirects=True, stream=True)

        if r.status_code != 200:
            print(f"  ✗ HTTP {r.status_code}")
            return False

        # A genuine file download is served as an attachment. Box's error/login
        # pages are returned as inline HTML without this header, so we use it to
        # tell a real download apart from an error page. This correctly accepts
        # files that are themselves HTML (e.g. ``*.html``).
        disposition = r.headers.get("content-disposition", "")
        is_attachment = "attachment" in disposition.lower()

        output_path.parent.mkdir(parents=True, exist_ok=True)

        first = True
        total = 0
        with open(output_path, "wb") as fh:
            for chunk in r.iter_content(chunk_size=65536):
                if not chunk:
                    continue
                if first and not is_attachment:
                    head = chunk[:20].strip().lower()
                    if head.startswith(b"<!doctype") or head.startswith(b"<html"):
                        print("  ✗ Received HTML instead of file content")
                        fh.close()
                        output_path.unlink(missing_ok=True)
                        return False
                first = False
                fh.write(chunk)
                total += len(chunk)

        print(f"  ✓ {output_path} ({total:,} bytes)")
        return True

    except Exception as e:  # noqa: BLE001 - report and keep going
        print(f"  ✗ {output_path}: {e}")
        output_path.unlink(missing_ok=True)
        return False


def download_all(
    output_dir: str = "docs",
    max_bytes: int = DEFAULT_MAX_BYTES,
    shared_link: str = SHARED_LINK,
    root_folder_id: str | None = None,
) -> int:
    """
    Download all files from the Box shared folder (including subfolders).

    Args:
        output_dir: Directory to save downloaded files.
        max_bytes: Skip files larger than this size (0 = no limit).
        shared_link: Box shared link or bare token to crawl.
        root_folder_id: Root folder id; auto-discovered from the page if None.

    Returns:
        Number of successfully downloaded files.
    """
    out_root = Path(output_dir)
    out_root.mkdir(parents=True, exist_ok=True)
    out_root_resolved = out_root.resolve()

    session = _new_session()
    token = _extract_token(shared_link)

    if root_folder_id is None:
        root_folder_id = _discover_root_folder_id(session, token)

    print(f"Shared folder: https://byu.box.com/s/{token}")
    print(f"Root folder id: {root_folder_id}")
    print(f"Output directory: {output_dir}")
    print()

    print("Discovering files (crawling subfolders)...")
    files = discover_files(session, token, root_folder_id)

    if not files:
        print("✗ No files found in shared folder.")
        return 0

    total_bytes = sum(f["size"] or 0 for f in files)
    print(f"Found {len(files)} file(s), {total_bytes:,} bytes total.")
    print()

    print("Downloading...")
    successes = 0
    skipped = 0
    for f in files:
        output_path = out_root / f["path"]
        size = f["size"] or 0

        # Guard against path traversal: file/folder names come from a remote
        # source, so ensure the resolved destination stays within out_root.
        try:
            output_path.resolve().relative_to(out_root_resolved)
        except ValueError:
            print(f"  ✗ unsafe path rejected: {f['path']}")
            continue

        if max_bytes and size > max_bytes:
            print(
                f"  ⤵ skipping {f['path']} "
                f"({size:,} bytes > {max_bytes:,} byte limit)"
            )
            skipped += 1
            continue

        # Resume support: skip files already downloaded at the expected size.
        if output_path.exists() and size and output_path.stat().st_size == size:
            print(f"  = {output_path} (already downloaded)")
            successes += 1
            continue

        if download_file(session, f["id"], output_path, token):
            successes += 1

    print()
    print(
        f"✓ Downloaded {successes}/{len(files)} file(s) to '{output_dir}/'"
        + (f" ({skipped} skipped over size limit)" if skipped else "")
    )
    return successes


def main():
    parser = argparse.ArgumentParser(
        description="Download documentation from Box shared folder: " + SHARED_LINK
    )
    parser.add_argument(
        "--output-dir",
        default="docs",
        help="Output directory for downloaded files (default: docs)",
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=DEFAULT_MAX_BYTES,
        help=(
            "Skip files larger than this many bytes (default: 100 MiB, the "
            "GitHub per-file limit). Use 0 to download everything."
        ),
    )

    parser.add_argument(
        "--shared-link",
        default=SHARED_LINK,
        help=(
            "Box shared link or bare token to crawl "
            "(default: the induction-furnace documentation folder)."
        ),
    )
    parser.add_argument(
        "--root-folder-id",
        default=None,
        help=(
            "Root folder id of the shared link. Auto-discovered from the "
            "shared link landing page if not provided."
        ),
    )

    args = parser.parse_args()

    count = download_all(
        args.output_dir,
        args.max_bytes,
        shared_link=args.shared_link,
        root_folder_id=args.root_folder_id,
    )
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())
