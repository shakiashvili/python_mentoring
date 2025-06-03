import logging
from bs4 import BeautifulSoup
from tools.http_client import HTTPClient
logging.basicConfig(level=logging.INFO, filename='tool.log',
                    format="%(asctime)s - %(levelname)s - %(message)s")


class CatsAnalyzer(HTTPClient):
    def __init__(self, endpoint: str) -> None:
        super().__init__(endpoint)

    def get_endpoint_status_code(self, path=None) -> int:
        response = self.get(path)
        logging.info(f'{response.url}, {response.status_code}')

        return response.status_code

    def get_h1_text(self, element: str = 'h1', path=None,
                    classname=None) -> str:

        response = self.get(path)
        soup = BeautifulSoup(response.text, 'html.parser')
        if classname:
            data = soup.find(element, class_=classname)
        else:
            data = soup.find(element)
        if data:
            logging.info(data.text)
            return data.text
