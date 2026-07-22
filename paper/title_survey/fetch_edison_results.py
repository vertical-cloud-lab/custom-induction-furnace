"""Fetch the Edison analysis task result once (no polling loop).

Run from paper/title_survey/:  python3 fetch_edison_results.py
Prints the task status. When the task is done, writes:
  edison_title_feedback.md  -- the answer/report
  artifacts/                -- any files attached to the trajectory
"""
import json
import os
import pathlib

from edison_client import EdisonClient


def main():
    task_id = open("edison_task_id.txt").read().strip()
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    task = client.get_task(task_id, verbose=True)
    status = str(getattr(task, "status", "unknown"))
    print("status:", status)
    if status.lower() not in {"success", "completed", "done", "failure", "failed"}:
        return

    dump = task.model_dump(mode="json")
    with open("edison_task_response.json", "w") as f:
        json.dump(dump, f, indent=1, default=str)

    answer = None
    for attr in ("answer", "formatted_answer", "response", "result"):
        answer = getattr(task, attr, None) or (dump.get(attr) if isinstance(dump, dict) else None)
        if answer:
            break
    if answer is None:
        # PQA-style responses nest the answer inside environment frame state.
        frame = dump.get("environment_frame") or {}
        answer = json.dumps(frame, indent=1, default=str)[:20000]
    with open("edison_title_feedback.md", "w") as f:
        f.write(str(answer))
    print("wrote edison_title_feedback.md")

    artifacts_dir = pathlib.Path("artifacts")
    try:
        files = client.list_files(task_id)
        print("trajectory files:", files)
        artifacts_dir.mkdir(exist_ok=True)
        file_list = files.get("files", files) if isinstance(files, dict) else files
        for entry in file_list or []:
            name = entry.get("name") if isinstance(entry, dict) else str(entry)
            try:
                data = client.fetch_data_from_storage(task_id, name)
                out = artifacts_dir / os.path.basename(name)
                mode = "wb" if isinstance(data, (bytes, bytearray)) else "w"
                with open(out, mode) as f:
                    f.write(data)
                print("saved", out)
            except Exception as e:  # noqa: BLE001
                print(f"could not fetch {name}: {e}")
    except Exception as e:  # noqa: BLE001
        print("artifact listing failed:", e)


if __name__ == "__main__":
    main()
