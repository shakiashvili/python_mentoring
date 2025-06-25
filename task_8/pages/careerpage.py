from locators import Locators
from basepage import BasePage


class CareerPage(BasePage):

    def enter_career(self, value: str) -> None:
        self.find_element(Locators.careers_link).click()
        self.find_element(Locators.remote_option).click()
        self.find_element(Locators.keyword_field).send_keys(value)
        self.find_element(Locators.location_dropdown).click()
        self.find_element(Locators.all_locations).click()
        self.find_element(Locators.submit_button).click()

    def get_title_of_last_item_on_page(self) -> str:
        self.find_element(Locators.last_elemenet).click()
        return self.find_element(Locators.position_detail).text
