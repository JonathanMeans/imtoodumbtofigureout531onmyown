from django.contrib.auth.models import User
from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import FiveThreeOneFunctionalTest, HomePage


class SimpleWorkoutTest(FiveThreeOneFunctionalTest):
    def test_can_start_workout_and_see_plan(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)
        page = HomePage(self.browser)

        # She enters her training max for deadlift and selects week 2
        page.submit_training_max("425", 2)

        # She sees her first set of deadlifts
        deadlift_table = WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element_by_id("id_workout_table")
        )
        rows = deadlift_table.find_elements_by_tag_name("td")
        rows = [row.text for row in rows]
        self.assertEqual(rows[0], "40%")

        # And it has all the sets for the workout
        self.assertEqual(rows[40], "70%")
        self.assertEqual(rows[41], "5")
        self.assertEqual(rows[42], "297.5")

        # The first set is highlighted to show where she is in the workout
        rows = deadlift_table.find_element_by_tag_name(
            "tbody"
        ).find_elements_by_tag_name("tr")
        first_row = rows[0]
        self.assertIn("current-set", first_row.get_attribute("class").split())

        # But not the second set
        second_row = rows[1]
        self.assertNotIn("current-set", second_row.get_attribute("class").split())

        # She clicks the "complete set" button and the highlighted set advances
        self.browser.find_element_by_id("id_next_set").click()
        self.assertIn("current-set", second_row.get_attribute("class").split())

    def test_can_save_and_load_an_exercise(self):
        User.objects.create_user("Shantae", "shantae@google.com", "password")

        # Shantae goes to her training website to start her workout
        self.browser.get(self.live_server_url)
        page = HomePage(self.browser)
        page.submit_training_max("425", 2)

        # When she's done, she saves her exercise so she can come back to it
        exercise_input = self.browser.find_element_by_id("id_name")
        exercise_input.send_keys("Deadlift")
        tmax_input = self.browser.find_element_by_id("id_new_lift_training_max")
        tmax_input.send_keys("425")
        week_input = self.browser.find_element_by_id("id_new_lift_week_number")
        week_input.send_keys("2")
        save_exercise_button = self.browser.find_element_by_id("id_submit_new_lift")
        save_exercise_button.click()

        # She can now see the name of the exercise and her training max on a new page
        first_lift = WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element_by_link_text("Deadlift - 425: Week 2")
        )

        # She clicks on the Deadlift to go back to the page for that exercise
        first_lift.click()
        deadlift_table = WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element_by_id("id_workout_table")
        )
        rows = deadlift_table.find_elements_by_tag_name("td")
        rows = [row.text for row in rows]
        self.assertEqual(rows[2], "170.0")
