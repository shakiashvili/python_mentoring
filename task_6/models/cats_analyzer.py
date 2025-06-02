import logging
from bs4 import BeautifulSoup
from tools.httpclient import HTTPClient
logging.basicConfig(level=logging.INFO, filename='tool.log',
                    format="%(asctime)s - %(levelname)s - %(message)s")


class CatsAnalyzer(HTTPClient):
    def __init__(self, endpoint):
        super().__init__(endpoint)

    def status_code_analyzer(self, method, path=None):
        if not path:
            response = method()
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
