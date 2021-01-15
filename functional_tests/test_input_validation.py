import time

from functional_tests.base import FiveThreeOneFunctionalTest


class ValidationTest(FiveThreeOneFunctionalTest):
    def test_only_able_to_enter_valid_weights(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)

        # She is asked to enter her training max for deadlift
        inputbox = self.browser.find_element_by_id("id_tmax_input")

        # She mistypes and doesn't enter a number
        inputbox.send_keys("4a25")
        self.browser.find_element_by_id("id_submit_tmax").click()

        time.sleep(0.5)

        # She sees an error message about her invalid input
        error_message = self.browser.find_element_by_id("tmax_error").text
        self.assertContains(error_message, "4a25")
