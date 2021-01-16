from django.test import TestCase

from five_three_one.forms import TrainingMaxForm


class TestHomeView(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_uses_tmax_form(self) -> None:
        response = self.client.get("/")
        self.assertIsInstance(response.context["form"], TrainingMaxForm)


class TestWorkoutView(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.post("/workout", data={"training_max": "170"})
        self.assertTemplateUsed(response, "home.html")

    def test_shows_deadlift_workout(self) -> None:
        response = self.client.post("/workout", data={"training_max": "425"})
        self.assertContains(response, "40%")
        self.assertContains(response, "5")
        self.assertContains(response, "170")
        self.assertContains(response, "45x1")
