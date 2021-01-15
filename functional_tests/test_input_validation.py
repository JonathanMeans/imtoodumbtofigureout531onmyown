from typing import cast

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from functional_tests.base import FiveThreeOneFunctionalTest


class HomePage:
    def __init__(self, browser: WebDriver) -> None:
        self.browser = browser

    def get_training_max_input(self) -> WebElement:
        return self.browser.find_element_by_id("id_training_max")

    def submit_training_max(self, tmax_value: str) -> None:
        inputbox = self.get_training_max_input()
        inputbox.send_keys(tmax_value)
        self.browser.find_element_by_id("id_submit_tmax").click()

    def get_validation_message(self) -> str:
        inputbox = self.get_training_max_input()
        return cast(str, inputbox.get_attribute("validationMessage"))


class ValidationTest(FiveThreeOneFunctionalTest):
    def test_only_able_to_enter_valid_weights(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)
        page = HomePage(self.browser)

        # She is asked to enter her training max for deadlift
        # She enters a number far too low
        page.submit_training_max("25")

        # She sees an error message about her invalid input
        error_message = page.get_validation_message()
        self.assertIn("112.5", error_message)
