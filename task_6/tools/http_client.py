import requests
from urllib.parse import urljoin


class HTTPClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def get(self, path=None) -> requests.Response:
        full_url = urljoin(self.endpoint, path if path else '')
        response = requests.get(full_url)
        return response

    def post(self, path: str, **kwargs) -> requests.Response:
        full_url = urljoin(self.endpoint, path)
        response = requests.post(full_url, kwargs)
        return response

    def put(self, path: str, **kwargs) -> requests.Response:
        full_url = urljoin(self.endpoint, path)
        return requests.put(full_url, kwargs)

    def delete(self, path: str) -> requests.Response:
        full_url = urljoin(self.endpoint, path)
        response = requests.delete(full_url)
        return response
