import pytest
import yaml
from selenium import webdriver


@pytest.fixture
def extract_yml():
    with open('env.yaml') as f:
        return yaml.safe_load(f)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver


@pytest.fixture
def go_to_website(extract_yml, driver) -> None:
    value = extract_yml.get('base_url')
    driver.get(value)


@pytest.fixture
def get_programming_language(extract_yml) -> str:
    return extract_yml.get('language')
