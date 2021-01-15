import os

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class FiveThreeOneFunctionalTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        staging_server = os.environ.get("STAGING_SERVER")
        if staging_server:
            self.live_server_url = f"http://{staging_server}"  # type: ignore

    def tearDown(self) -> None:
        self.browser.quit()
