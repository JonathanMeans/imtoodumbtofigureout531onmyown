import time

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


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
        self.browser.find_element_by_id("id_submit_tmax").click()

        # She sees her first set of deadlifts
        time.sleep(2)
        deadlift_table = self.browser.find_element_by_id("id_deadlift_week_one")
        rows = deadlift_table.find_elements_by_tag_name("td")
        rows = [row.text for row in rows]
        self.assertEqual(rows[0], "40%")
