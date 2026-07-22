"""Fetch the Edison no-prep-EBSD literature task result once (no polling loop).

Run from paper/ebsd_noprep_query/:  python3 fetch_results.py
Prints the task status. When the task is done, writes:
  edison_noprep_ebsd_report.md -- the answer/report
  edison_task_response.json    -- full task response for provenance
  artifacts/                   -- files attached to the trajectory, if any
"""
import json
import os
import pathlib

from edison_client import EdisonClient


def main():
    task_id = open("edison_task_id.txt").read().strip()
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    task = client.get_task(task_id, history=True)
    status = str(getattr(task, "status", "unknown"))
    print("status:", status)
    if status.lower() not in {"success", "completed", "done", "failure", "failed", "fail"}:
        return

    dump = task.model_dump(mode="json")
    with open("edison_task_response.json", "w") as f:
        json.dump(dump, f, indent=1, default=str)

    answer = dump.get("answer") or getattr(task, "answer", None)
    if answer:
        with open("edison_noprep_ebsd_report.md", "w") as f:
            f.write(str(answer))
        print("wrote edison_noprep_ebsd_report.md")
    else:
        print("no answer field present")

    artifacts_dir = pathlib.Path("artifacts")
    artifacts_dir.mkdir(exist_ok=True)
    try:
        files = client.list_files(task_id)
    except Exception as e:  # noqa: BLE001
        print("list_files failed:", e)
        return
    for entry in files.get("data", []):
        ds = entry.get("data_storage", {})
        ds_id, name = ds.get("id"), ds.get("name", "unnamed")
        try:
            result = client.fetch_data_from_storage(ds_id)
            if isinstance(result, pathlib.Path):
                result.rename(artifacts_dir / result.name)
                print("saved", artifacts_dir / result.name)
            elif isinstance(result, list):
                for p in result:
                    p.rename(artifacts_dir / p.name)
                    print("saved", artifacts_dir / p.name)
            else:
                content = getattr(result, "content", None) or getattr(result, "data", None)
                out = artifacts_dir / name
                if isinstance(content, (bytes, bytearray)):
                    out.write_bytes(content)
                else:
                    out.write_text(str(content))
                print("saved", out)
        except Exception as e:  # noqa: BLE001
            print(f"could not fetch {name} ({ds_id}): {e}")


if __name__ == "__main__":
    main()
