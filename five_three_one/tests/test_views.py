from django.test import TestCase

from five_three_one.forms import TrainingMaxForm


class TestHomeView(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_uses_tmax_form(self) -> None:
        response = self.client.get("/")
        self.assertIsInstance(response.context["form"], TrainingMaxForm)

    def test_POST_uses_tmax_form(self) -> None:
        response = self.client.post("/", data={"training_max": "170"})
        self.assertIsInstance(response.context["form"], TrainingMaxForm)

    def test_error_on_alpha_tmax(self) -> None:
        response = self.client.post(
            "/", data={"training_max": "abc", "week_number": "1"}
        )
        self.assertIn("Enter a number", response.context["errors"]["training_max"][0])

    def test_error_on_too_small_tmax(self) -> None:
        response = self.client.post(
            "/", data={"training_max": "50", "week_number": "1"}
        )
        self.assertIn(
            "greater than or equal to", response.context["errors"]["training_max"][0]
        )

    def test_POST_uses_home_template(self) -> None:
        response = self.client.post("/", data={"training_max": "170"})
        self.assertTemplateUsed(response, "home.html")

    def test_POST_shows_deadlift_workout(self) -> None:
        response = self.client.post(
            "/", data={"training_max": "425", "week_number": "1"}
        )
        self.assertContains(response, "40%")
        self.assertContains(response, "5")
        self.assertContains(response, "170")
        self.assertContains(response, "45x1")
