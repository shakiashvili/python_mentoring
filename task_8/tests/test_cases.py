import pytest
import yaml
from pages.searchpage import SearchPage
from pages.careerpage import CareerPage

with open("env.yaml") as f:
    testdata = yaml.safe_load(f).get("testdata", [])


def test_career_page(go_to_website, driver, get_programming_language) -> None:
    career_page = CareerPage(driver)
    career_page.accept_cookies()
    career_page.enter_career(get_programming_language)
    title = career_page.get_title_of_last_item_on_page()
    assert get_programming_language in title


@pytest.mark.parametrize('params', testdata)
def test_second_suite(go_to_website, driver, params: str) -> None:
    search_page = SearchPage(driver)
    search_page.accept_cookies()
    links = search_page.search_text(params)
    for link in links:
        assert params in link.text, f"{params}' not in: {link.text}"
