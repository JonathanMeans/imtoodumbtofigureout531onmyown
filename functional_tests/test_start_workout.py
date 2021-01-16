from selenium.webdriver.support.wait import WebDriverWait

from functional_tests.base import FiveThreeOneFunctionalTest, HomePage


class SimpleWorkoutTest(FiveThreeOneFunctionalTest):
    def test_can_start_workout_and_see_plan(self) -> None:
        # Shantae goes to her training website to try out the 531 for beginners workout
        self.browser.get(self.live_server_url)
        page = HomePage(self.browser)

        # She enters her training max for deadlift
        page.submit_training_max("425")

        # She sees her first set of deadlifts
        deadlift_table = WebDriverWait(self.browser, 10).until(
            lambda browser: browser.find_element_by_id("id_workout_table")
        )
        # self.browser.find_element_by_id("id_workout_table")
        rows = deadlift_table.find_elements_by_tag_name("td")
        rows = [row.text for row in rows]
        self.assertEqual(rows[0], "40%")

        # And it has all the sets for the workout
        self.assertEqual(rows[40], "65%")
        self.assertEqual(rows[41], "5")
        self.assertEqual(rows[42], "275.0")

        # The first set is highlighted to show where she is in the workout
        rows = deadlift_table.find_element_by_tag_name(
            "tbody"
        ).find_elements_by_tag_name("tr")
        first_row = rows[0]
        self.assertIn("current-set", first_row.get_attribute("class").split())

        # But not the second set
        second_row = rows[1]
        self.assertNotIn("current-set", second_row.get_attribute("class").split())
