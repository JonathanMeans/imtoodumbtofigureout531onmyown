from django import forms


class TrainingMaxForm(forms.Form):
    training_max = forms.FloatField(min_value=112.5)
    week_number = forms.IntegerField(min_value=1, max_value=3)
