import requests
from sys import argv
import os
from multiprocessing import Pool
from progressbars import ProgressBars


def sender():
    filenames = [f"test_data/test_data_{i}.txt" for i in range(6)]
    with Pool(6) as pool:
        pool.map(send_events, filenames)


def send_events(filename):
    progress_bars = ProgressBars()
    location = int(filename[20])
    file = open(filename, "r")
    scripts, url, auth = argv
    headers = {"x": auth}
    pid = f"process:{os.getpid()}"
    progress_bars.add_task(pid)
    for line in file:
        progress_bars.increment_task(pid, location)
        requests.post(url, json=line, headers=headers)


if __name__ == "__main__":
    sender()
