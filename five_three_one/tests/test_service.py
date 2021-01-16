from unittest import TestCase

from five_three_one.services import get_workout


class TestWorkoutService(TestCase):
    def test_can_retrieve_week_1_workout(self) -> None:
        training_max = 425
        workout = get_workout(training_max, 1)
        self.assertEqual(11, len(workout))
        first_set = workout[0]
        self.assertEqual(first_set.percent, "40%")
        self.assertEqual(first_set.reps, "5")
        self.assertEqual(first_set.weight, 170)
        self.assertEqual(first_set.breakdown, "45x1, 10x1, 5x1, 2.5x1")

    def test_can_retrieve_week_2_workout(self) -> None:
        training_max = 425
        workout = get_workout(training_max, 2)
        self.assertEqual(11, len(workout))
        first_set = workout[0]
        self.assertEqual(first_set.percent, "40%")
        self.assertEqual(first_set.reps, "5")
        self.assertEqual(first_set.weight, 170)
        self.assertEqual(first_set.breakdown, "45x1, 10x1, 5x1, 2.5x1")

        last_set = workout[10]
        self.assertEqual(last_set.percent, "70%")
        self.assertEqual(last_set.reps, "5")
        self.assertEqual(last_set.weight, 297.5)
        self.assertEqual(last_set.breakdown, "45x2, 25x1, 10x1, 1.25x1")
