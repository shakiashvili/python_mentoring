import requests
from urllib.parse import urljoin

class HTTPClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, path: str):
        full_url = urljoin(self.endpoint, path)
        response = requests.get(full_url)
        return response

    def post(self, path: str, **kwargs):
        full_url = urljoin(self.endpoint, path)
        response = requests.post(full_url, kwargs)
        return response

    def put(self, path: str, **kwargs):
        full_url = urljoin(self.endpoint, path)
        response = requests.put(full_url, kwargs)
        return response

    def delete(self, path: str):
        full_url = urljoin(self.endpoint, path)
        requests.delete(full_url)
