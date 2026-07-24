"""Foreground-blocking poller for the Edison review task (per CLAUDE.md:
never poll Edison in the background on GitHub Actions runners). Checks the
task status every 2 min until it leaves the running states or MAX_WAIT_S
elapses, then exits; run fetch_results.py afterwards to retrieve outputs.

Run from paper/manuscript_review_query/:  python3 poll_until_done.py
"""
import os
import time

from edison_client import EdisonClient

MAX_WAIT_S = 35 * 60
INTERVAL_S = 120
RUNNING = {"in progress", "queued", "pending", "running", "submitted"}


def main():
    task_id = open("edison_task_id.txt").read().strip()
    client = EdisonClient(api_key=os.environ["EDISON_PLATFORM_API_KEY"])
    start = time.time()
    while True:
        status = str(getattr(client.get_task(task_id), "status", "unknown"))
        elapsed = int(time.time() - start)
        print(f"[{elapsed:4d}s] status: {status}", flush=True)
        if status.lower() not in RUNNING:
            print("terminal status reached")
            return
        if elapsed > MAX_WAIT_S:
            print("gave up after max wait; task still running")
            return
        time.sleep(INTERVAL_S)


if __name__ == "__main__":
    main()
