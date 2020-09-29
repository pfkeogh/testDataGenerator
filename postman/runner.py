import os
import json
from sys import argv
from postman.request import RequestTemplate
from multiprocessing import Pool
from functools import partial
import requests



# pass the postman filename and number of requests to make
def main():
    script, filename, number_of_requests = argv
    postman_json = read_file(filename)
    request_templates = request_builder(postman_json)
    multiprocess_runner(request_templates, number_of_requests)


def multiprocess_runner(request_templates, number_of_requests):
    pool = Pool(len(request_templates))
    request_send = partial(request_sender, number_of_requests=number_of_requests)
    pool.map(request_send, request_templates)


def request_sender(request_template: RequestTemplate, number_of_requests):
    pid = f"process:{os.getpid()} request: {request_template.name} method: {request_template.method}"
    for i in range(0, int(number_of_requests)):
        requests.post(request_template.url, data=request_template.data, headers=request_template.headers)
    print(f'{pid} complete')


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
