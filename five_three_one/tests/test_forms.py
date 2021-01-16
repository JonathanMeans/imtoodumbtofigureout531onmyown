from django.test import TestCase

from five_three_one.forms import TrainingMaxForm


class TrainingMaxFormTest(TestCase):
    def test_validation_error_for_nonnumeric_data(self) -> None:
        form = TrainingMaxForm(data={"training_max": "abc"})
        self.assertFalse(form.is_valid())
        self.assertIn("Enter a number", form.errors["training_max"][0])

    def test_validation_error_for_too_small_number(self) -> None:
        form = TrainingMaxForm(data={"training_max": "45"})
        self.assertFalse(form.is_valid())
        self.assertIn("112.5", form.errors["training_max"][0])