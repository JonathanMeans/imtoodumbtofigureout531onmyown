from unittest import skip

from django.test import TestCase

from five_three_one.services import get_workout


class TestHomeView(TestCase):
    def test_uses_home_template(self) -> None:
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")


class TestWorkoutView(TestCase):
    def test_uses_workout_template(self) -> None:
        response = self.client.post("/workout")
        self.assertTemplateUsed(response, "workout.html")

    @skip("service not implemented")
    def test_shows_deadlift_workout(self) -> None:
        response = self.client.post("/workout", data={"deadlift": "170"})
        self.assertContains(response, "40%")
        self.assertContains(response, "5")
        self.assertContains(response, "170")
        self.assertContains(response, "45x1")


class TestWorkoutService(TestCase):
    def test_can_retrieve_deadlift_workout(self) -> None:
        training_max = 425
        workout = get_workout(training_max)
        self.assertEqual(workout.percent, "40%")
        self.assertEqual(workout.reps, 5)
        self.assertEqual(workout.weight, 170)
        self.assertEqual(workout.breakdown, "45x1, 10x1, 5x1, 2.5x1")
