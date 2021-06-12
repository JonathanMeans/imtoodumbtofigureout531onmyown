from functional_tests.base import FiveThreeOneFunctionalTest, HomePage


class ValidationTest(FiveThreeOneFunctionalTest):
    def test_only_able_to_enter_valid_weights(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)
        page = HomePage(self.browser)

        # She is asked to enter her training max for deadlift
        # She enters a number far too low
        page.submit_training_max("Deadlift", "25", 1)

        # She sees an error message about her invalid input
        error_message = page.get_validation_message()
        self.assertIn("112.5", error_message)
