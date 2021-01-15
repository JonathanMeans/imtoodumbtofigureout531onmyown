from functional_tests.base import FiveThreeOneFunctionalTest


class ValidationTest(FiveThreeOneFunctionalTest):
    def test_only_able_to_enter_valid_weights(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)

        # She is asked to enter her training max for deadlift
        inputbox = self.browser.find_element_by_id("id_training_max")

        # She mistypes and doesn't enter a number
        inputbox.send_keys("25")
        self.browser.find_element_by_id("id_submit_tmax").click()

        # She sees an error message about her invalid input
        error_message = inputbox.get_attribute("validationMessage")
        self.assertIn("112.5", error_message)
