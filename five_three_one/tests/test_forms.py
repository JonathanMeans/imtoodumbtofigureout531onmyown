from django.test import TestCase

from five_three_one.forms import TrainingMaxForm, NewLiftForm


class TrainingMaxFormTest(TestCase):
    def test_validation_error_for_nonnumeric_data(self) -> None:
        form = TrainingMaxForm(data={"training_max": "abc"})
        self.assertFalse(form.is_valid())
        self.assertIn("Enter a number", form.errors["training_max"][0])

    def test_validation_error_for_too_small_number(self) -> None:
        form = TrainingMaxForm(data={"training_max": "45"})
        self.assertFalse(form.is_valid())
        self.assertIn("112.5", form.errors["training_max"][0])

    def test_validation_error_for_invalid_week(self) -> None:
        form = TrainingMaxForm(data={"training_max": "425", "week_number": "0"})
        self.assertFalse(form.is_valid())
        self.assertIn("greater than or equal to 1", form.errors["week_number"][0])

        form = TrainingMaxForm(data={"training_max": "425", "week_number": "4"})
        self.assertFalse(form.is_valid())
        self.assertIn("less than or equal to 3", form.errors["week_number"][0])


class NewLiftFormTest(TestCase):
    def test_new_lift_form_has_custom_field_names(self):
        form = NewLiftForm()
        # Need to disambiguate from training_max field of TrainingMaxForm
        self.assertNotIn("id_training_max", form.as_p())
        self.assertIn("id_new_lift_training_max", form.as_p())

        self.assertNotIn("id_week_number", form.as_p())
        self.assertIn("id_new_lift_week_number", form.as_p())
