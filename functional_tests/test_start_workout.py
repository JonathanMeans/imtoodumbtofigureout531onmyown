from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class SimpleWorkoutTest(StaticLiveServerTestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_workout_and_see_plan(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)

        # She is asked to enter her training max for deadlift
        inputbox = self.browser.find_element_by_id("id_deadlift_tmax_input")

        # She enters her impressive starting point
        inputbox.send_keys("425")
        inputbox.send_keys(Keys.ENTER)
