import requests
import time
import csv
from datetime import datetime

TARGETS = ["https://example.com", "https://github.com"]
LOG = "uptime.csv"


def check(url):
    start = time.time()
    try:
        r = requests.get(url, timeout=5)
        return r.status_code, round((time.time() - start) * 1000)
    except requests.RequestException:
        return None, None


def run():
    with open(LOG, "a", newline="") as f:
        writer = csv.writer(f)
        for url in TARGETS:
            status, ms = check(url)
            writer.writerow([datetime.now().isoformat(), url, status, ms])
            print(f"{url} -> {status} ({ms}ms)")


if __name__ == "__main__":
    run()
