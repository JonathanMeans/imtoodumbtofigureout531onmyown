from typing import Optional

from django.forms.utils import ErrorDict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from five_three_one.forms import TrainingMaxForm
from five_three_one.services import get_workout


def home_view(request: HttpRequest) -> HttpResponse:
    workout = None
    errors: Optional[ErrorDict] = None
    if request.method == "POST":
        tmax_form = TrainingMaxForm(request.POST)
        if tmax_form.is_valid():
            training_max = float(request.POST["training_max"])
            week_number = int(request.POST["week_number"])
            workout = get_workout(training_max, week_number)
        else:
            errors = tmax_form.errors
    return render(
        request,
        "home.html",
        {"workout": workout, "form": TrainingMaxForm(), "errors": errors},
    )
