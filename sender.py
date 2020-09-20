import requests
from sys import argv
import os
from multiprocessing import Pool
import time
from blessings import Terminal


class Progress:
    bar = [
        " [ | ]",
        " [ \ ]",
        " [ - ]",
        " [ / ]",
    ]

    def __init__(self):
        self.term = Terminal()
        self.bars = {}
        self.bars_increment = {}

    def add_task(self, task_name):
        self.bars[task_name] = self.bar[0]
        self.bars_increment[task_name] = 0

    def increment_task(self, task_name, location):
        i = self.bars_increment[task_name]
        self.bars[task_name] = self.bar[i % len(self.bar)]
        self.bars_increment[task_name] += 1
        with self.term.location(0, self.term.height - (location+1)):
            print(self.view(), end="\r")

    def view(self):
        progress_string = ""
        for key, val in self.bars.items():
            progress_string += f"  {key}:{val}  "
        return progress_string


def sender():
    filenames = [f"test_data/test_data_{i}.txt" for i in range(6)]
    with Pool(6) as pool:
        pool.map(send_events, filenames)


def send_events(filename):
    progress_bars = Progress()
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
    Terminal().clear()
