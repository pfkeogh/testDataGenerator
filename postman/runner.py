import os
import json
from sys import argv
from postman.request import RequestTemplate
from multiprocessing import Pool
from progressbars import ProgressBars


# pass the postman filename and number of requests to make
def main():
    script, filename, number_of_requests = argv
    postman_json = read_file(filename)
    request_templates = request_builder(postman_json)
    multiprocess_runner(request_templates, number_of_requests)


def multiprocess_runner(request_templates, number_of_requests):
    with Pool(len(request_templates)) as pool:
        pool.map(request_sender, request_templates, number_of_requests)


def request_sender(request_template, number_of_requests):
    progress_bars = ProgressBars()
    pid = f"process:{os.getpid()}"
    progress_bars.add_task(pid)
    for i in range(0, number_of_requests):
        progress_bars.increment_task(pid, 1)
        # requests.post(url, json=line, headers=headers)
    print('thread ran')


def request_builder(postman_json):
    request_templates = []
    for item in postman_json['item']:
        request_templates.append(RequestTemplate(item))
    return request_templates


def read_file(filename):
    filename = open(filename, "r")
    postman_json = json.load(filename)
    return postman_json


if __name__ == "__main__":
    main()
