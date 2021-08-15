from django import forms
from django.forms import ModelForm, Form

from five_three_one.models import Lift


class NewLiftForm(ModelForm):
    class Meta:
        model = Lift
        fields = ["name", "training_max", "week_number"]
        widgets = {
            "training_max": forms.fields.NumberInput(
                attrs={"id": "id_new_lift_training_max", "min": 112.5}
            ),
            "week_number": forms.fields.NumberInput(
                attrs={
                    "id": "id_new_lift_week_number",
                    "min": 1,
                    "max": 3,
                    "initial": 1,
                }
            ),
        }

    def clean_training_max(self):
        training_max = self.cleaned_data["training_max"]
        min_value = self.fields["training_max"].widget.attrs["min"]
        if training_max < min_value:
            raise forms.ValidationError(
                f"Training max must be greater than or equal to {min_value}"
            )
        return training_max


class IncrementTmaxForm(Form):
    id = forms.IntegerField()
    increment = forms.FloatField()
