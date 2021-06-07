from django import forms
from django.forms import ModelForm

from five_three_one.models import Lift


class TrainingMaxForm(forms.Form):
    training_max = forms.FloatField(min_value=112.5)
    week_number = forms.IntegerField(min_value=1, max_value=3, initial=1)


class NewLiftForm(ModelForm):
    class Meta:
        model = Lift
        fields = ["name", "training_max", "week_number"]
        widgets = {
            "training_max": forms.fields.NumberInput(
                attrs={"id": "id_new_lift_training_max"}
            ),
            "week_number": forms.fields.NumberInput(
                attrs={"id": "id_new_lift_week_number"}
            )
        }
