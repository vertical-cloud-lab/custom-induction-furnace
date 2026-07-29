"""Fetch both Edison reviewer-suggestion tasks once (no polling loop).

Run from paper/reviewer_search/:  python3 fetch_results.py [--status-only]
For each finished task, writes:
  edison_<kind>_reviewers_report.md, edison_<kind>_task_response.json,
  artifacts_<kind>/ (trajectory artifacts).
"""
import json
import os
import pathlib
import sys

from edison_client import EdisonClient

TASKS = [
    ("analysis", "edison_analysis_task_id.txt"),
    ("literature", "edison_literature_task_id.txt"),
]
DONE = {"success", "completed", "done"}
FAILED = {"failure", "failed", "fail"}


def fetch(client, kind, task_id, status_only):
    try:
        task = client.get_task(task_id, history=False)
    except Exception as e:  # noqa: BLE001
        print(f"{kind}: get_task failed: {e}")
        return "error"
    status = str(getattr(task, "status", "unknown")).lower()
    print(f"{kind}: {status}")
    if status_only or status not in DONE | FAILED:
        return status

    dump = task.model_dump(mode="json")
    with open(f"edison_{kind}_task_response.json", "w") as f:
        json.dump(dump, f, indent=1, default=str)
    answer = dump.get("answer")
    if answer:
        with open(f"edison_{kind}_reviewers_report.md", "w") as f:
            f.write(str(answer))
        print(f"wrote edison_{kind}_reviewers_report.md")

    art = pathlib.Path(f"artifacts_{kind}")
    art.mkdir(exist_ok=True)
    try:
        files = client.list_files(task_id)
        for entry in files.get("data", []):
            ds = entry.get("data_storage", {})
            ds_id, name = ds.get("id"), ds.get("name", "unnamed")
            try:
                result = client.fetch_data_from_storage(ds_id)
                if isinstance(result, pathlib.Path):
                    result.rename(art / result.name)
                elif isinstance(result, list):
                    for p in result:
                        p.rename(art / p.name)
                else:
                    content = getattr(result, "content", None) or getattr(result, "data", None)
                    out = art / name
                    if isinstance(content, (bytes, bytearray)):
                        out.write_bytes(content)
                    else:
                        out.write_text(str(content))
                print("saved artifact:", name)
            except Exception as e:  # noqa: BLE001
                print(f"could not fetch {name}: {e}")
    except Exception as e:  # noqa: BLE001
        print("list_files failed:", e)
    return status


def main():
    status_only = "--status-only" in sys.argv
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    for kind, idfile in TASKS:
        task_id = open(idfile).read().strip()
        fetch(client, kind, task_id, status_only)


if __name__ == "__main__":
    main()
