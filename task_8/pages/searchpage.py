from locators import Locators
from .basepage import BasePage


class SearchPage(BasePage):

    def search_text(self, value: str):
        self.find_element(Locators.search_icon).click()
        self.find_element(Locators.search_keyword_field).clear()
        self.find_element(Locators.search_keyword_field).send_keys(value)
        self.find_element(Locators.find_button).click()
        return self.find_elements(Locators.links)
