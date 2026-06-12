#!/usr/bin/env python3
"""
Script to download documentation from Box shared folder.

This script downloads files from the Box shared link:
https://byu.box.com/s/lh04mmpkhvhy4vtokpm4sol711xycrph

The files are saved to the `docs/` directory.

Usage:
    python download_box_docs.py [--output-dir docs]

The script automatically discovers all files in the shared folder and
downloads them using Box's web download endpoint.
"""

import os
import sys
import argparse
import re
from pathlib import Path
from typing import Optional

try:
    import requests
except ImportError:
    print("❌ 'requests' package is required. Install with: pip install requests")
    sys.exit(1)


SHARED_TOKEN = "lh04mmpkhvhy4vtokpm4sol711xycrph"
SHARED_LINK = f"https://byu.box.com/s/{SHARED_TOKEN}"


def discover_files(session: "requests.Session") -> list[dict]:
    """
    Parse the Box shared folder page to discover all files.

    Args:
        session: requests.Session with cookies established.

    Returns:
        List of dicts with keys: id, name, size.
    """
    r = session.get(SHARED_LINK, timeout=20)
    r.raise_for_status()
    content = r.text

    # Extract file entries from the embedded JSON in the Box page
    # Each file appears as: "typedID":"f_<id>" ... "name":"<name>" ... "itemSize":<size>
    items = re.findall(
        r'"typedID":"f_(\d+)"[^{]*?"name":"([^"]+)"[^{]*?"itemSize":(\d+)',
        content,
    )

    files = [{"id": iid, "name": iname, "size": int(isize)} for iid, iname, isize in items]
    return files


def download_file(
    session: "requests.Session",
    file_id: str,
    file_name: str,
    output_dir: str,
) -> bool:
    """
    Download a single file from the Box shared folder.

    Args:
        session: requests.Session with cookies established.
        file_id: Box file ID.
        file_name: Name to save the file as.
        output_dir: Directory to save the file in.

    Returns:
        True if download succeeded, False otherwise.
    """
    download_url = (
        f"https://byu.app.box.com/index.php"
        f"?rm=box_download_shared_file"
        f"&shared_name={SHARED_TOKEN}"
        f"&file_id=f_{file_id}"
    )

    output_path = Path(output_dir) / file_name

    try:
        r = session.get(download_url, timeout=120, allow_redirects=True, stream=True)

        if r.status_code != 200:
            print(f"  ✗ HTTP {r.status_code}")
            return False

        content = b""
        for chunk in r.iter_content(chunk_size=65536):
            content += chunk

        # Reject HTML responses (Box web UI) instead of file content
        if content[:20].strip().lower().startswith(b"<!doctype") or content[:20].strip().lower().startswith(b"<html"):
            print(f"  ✗ Received HTML instead of file content")
            return False

        output_path.write_bytes(content)
        print(f"  ✓ {file_name} ({len(content):,} bytes)")
        return True

    except Exception as e:
        print(f"  ✗ {file_name}: {e}")
        return False


def download_all(output_dir: str = "docs") -> int:
    """
    Download all files from the Box shared folder.

    Args:
        output_dir: Directory to save downloaded files.

    Returns:
        Number of successfully downloaded files.
    """
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    session = requests.Session()
    session.headers.update(
        {
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            )
        }
    )

    print(f"Shared folder: {SHARED_LINK}")
    print(f"Output directory: {output_dir}")
    print()

    print("Discovering files...")
    try:
        files = discover_files(session)
    except Exception as e:
        print(f"✗ Failed to retrieve file list: {e}")
        return 0

    if not files:
        print("✗ No files found in shared folder.")
        return 0

    print(f"Found {len(files)} file(s):")
    for f in files:
        print(f"  {f['name']} ({f['size']:,} bytes)")
    print()

    print("Downloading...")
    successes = 0
    for f in files:
        if download_file(session, f["id"], f["name"], output_dir):
            successes += 1

    print()
    print(f"✓ Downloaded {successes}/{len(files)} file(s) to '{output_dir}/'")
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

    args = parser.parse_args()

    count = download_all(args.output_dir)
    return 0 if count > 0 else 1


if __name__ == "__main__":
    sys.exit(main())


