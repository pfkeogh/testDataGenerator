import os
import json
from sys import argv
from postman.request import RequestTemplate
from multiprocessing import Pool
from functools import partial
import requests
import time


# pass the postman filename and number of requests to make
# ex: python runner.py <filename> <number of requests>
def main():
    script, filename, number_of_requests = argv
    postman_json = read_file(filename)
    request_templates = request_builder(postman_json)
    start_time = time.time()
    multiprocess_runner(request_templates, number_of_requests)
    end_time = time.time()
    total_time = end_time - start_time
    total_requests = len(request_templates)*int(number_of_requests)
    results = f"{total_requests} requests made in {total_time} seconds. {round(float(total_requests)/total_time, 2)} requests per second\n"
    print(results)
    results_file = open('results.txt', 'a')
    results_file.write(results)
    results_file.close()


def multiprocess_runner(request_templates, number_of_requests):
    pool = Pool(len(request_templates))
    request_send = partial(request_sender, number_of_requests=number_of_requests)
    pool.map(request_send, request_templates)


def request_sender(request_template: RequestTemplate, number_of_requests):
    pid = f"process: {os.getpid()} request: {request_template.name} method: {request_template.method}"
    print(f'starting {pid}')
    for i in range(0, int(number_of_requests)):
        requests.post(request_template.url, data=request_template.data, headers=request_template.headers)
    print(f'completed {pid}')


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
