import logging
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

logging.basicConfig(level=logging.INFO, filename='tool.log',
                    format="%(asctime)s - %(levelname)s - %(message)s")


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


class CatsAnalyzer(HTTPClient):
    def __init__(self, endpoint):
        super().__init__(endpoint)

    def status_code_analyzer(self, method, path):
        response = method(path)
        logging.info(f'{response.url}, {response.status_code}')

        return response.status_code

    def analyze_text(self, method, element, path=None, classname=None):
        response = method(path)
        soup = BeautifulSoup(response.text, 'html.parser')
        if classname:
            data = soup.find(element, class_=classname)
        else:
            data = soup.find(element)
        if data:
            logging.info(data.text)
            return data.text
