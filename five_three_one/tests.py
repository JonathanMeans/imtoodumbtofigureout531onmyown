import sys
from unittest import skip

from django.test import TestCase

from five_three_one.services import get_workout


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


class TestWorkoutService(TestCase):
    def test_can_retrieve_deadlift_workout(self) -> None:
        training_max = 425
        workout = get_workout(training_max)
        self.assertEqual(11, len(workout))
        first_set = workout[0]
        self.assertEqual(first_set.percent, "40%")
        self.assertEqual(first_set.reps, 5)
        self.assertEqual(first_set.weight, 170)
        self.assertEqual(first_set.breakdown, "45x1, 10x1, 5x1, 2.5x1")
