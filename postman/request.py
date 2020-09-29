# import faker


class RequestTemplate:

    def __init__(self, postman_item):
        self.name = postman_item['name']
        self.url = postman_item['request']['url']['raw']
        self.method = postman_item['request']['method']
        self.headers = self.format_headers(postman_item['request']['header'])
        if self.method in ['POST', 'PUT', 'PATCH']:
            self.data = postman_item['request']['body']['raw']
        else:
            self.data = ''

    def get_data(self):
        print(self.name+' '+self.method)
        return self.data
        # TODO:look for random var and replace with faker data
        # TODO:use a generator

    @staticmethod
    def format_headers(headers: dict):
        formatted_headers = {}
        for header in headers:
            formatted_headers[header.get('key')] = header.get('value')
        return formatted_headers




