from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from locators import Locators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator: tuple) -> WebElement:
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: tuple) -> List[WebElement]:
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def accept_cookies(self) -> None:
        self.find_element(Locators.cookies).click()
