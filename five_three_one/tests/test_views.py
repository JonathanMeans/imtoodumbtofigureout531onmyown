from django.test import TestCase


class TestHomeView(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class TestWorkoutView(TestCase):
    def test_uses_workout_template(self) -> None:
        response = self.client.post("/workout", data={"tmax": "170"})
        self.assertTemplateUsed(response, "workout.html")

    def test_shows_deadlift_workout(self) -> None:
        response = self.client.post("/workout", data={"tmax": "425"})
        self.assertContains(response, "40%")
        self.assertContains(response, "5")
        self.assertContains(response, "170")
        self.assertContains(response, "45x1")
