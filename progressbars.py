from blessings import Terminal


class ProgressBars:
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
        with self.term.location(0, self.term.height - (location + 1)):
            print(self.view(), end="\r")

    def view(self):
        progress_string = ""
        for key, val in self.bars.items():
            progress_string += f"  {key}:{val}  "
        return progress_string
