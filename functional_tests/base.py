import os
from typing import cast

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class FiveThreeOneFunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = f"http://{staging_server}"  # type: ignore

    def tearDown(self) -> None:
        self.browser.quit()


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
