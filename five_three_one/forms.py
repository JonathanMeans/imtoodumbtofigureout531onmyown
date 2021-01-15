from django import forms


class TrainingMaxForm(forms.Form):
    training_max = forms.FloatField(min_value=112.5)
