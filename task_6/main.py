import requests 
from bs4 import BeautifulSoup
import html5lib


expected = "407 Proxy Authentication Required"
headers = {"Content-Type": "text/html"}

status_codes = [101, 202, 303, 407, 501]
for code in status_codes:
    url = f"https://http.cat/{code}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print('Successfully Executed')
    else:
        print('Failed to execute')
    if code == 407:
        soup = BeautifulSoup(response.content, 'html5lib')
        print()
        if soup.find('h1').text == expected:
            print("True", True)
        else:
            print("False")
