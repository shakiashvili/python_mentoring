import requests
import logging
from bs4 import BeautifulSoup


logging.basicConfig(level=logging.INFO, filename='tool.log',
                    format="%(asctime)s - %(levelname)s - %(message)s")

codes = [101, 202, 303, 407, 501]


def first_test_function():

    for code in codes:
        url = f"https://http.cat/status/{code}"

        response = requests.get(url)
        logging.info(f'{response.url}, {response.status_code}')

        assert response.status_code == 200

        soup = BeautifulSoup(response.text, 'lxml')

        if code == 407:

            data = soup.find('h1', class_='text-center my-12')

            logging.info(f'We get text from variable name: {data.name}')

            if data:
                assert data.text == "407 Proxy Authentication Required"


def second_test_function():
    url = "https://http.cat/status/"
    response = requests.get(url)
    logging.info(f'We got the response code {response.status_code}')
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('h1')
    logging.info(f'We get text from variable name: {data.name}')
    if data:
        assert data.text == '403 Forbidden'


if __name__ == '__main__':
    first_test_function()
    second_test_function()
