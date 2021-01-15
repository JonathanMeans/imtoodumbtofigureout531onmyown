from unittest import TestCase

from five_three_one.services import get_workout


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
