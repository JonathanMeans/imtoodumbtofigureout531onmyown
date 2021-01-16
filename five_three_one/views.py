from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from five_three_one.forms import TrainingMaxForm
from five_three_one.services import get_workout


def home_view(request: HttpRequest) -> HttpResponse:
    workout = None
    errors = ""
    if request.method == "POST":
        tmax_form = TrainingMaxForm(request.POST)
        if tmax_form.is_valid():
            training_max = float(request.POST["training_max"])
            workout = get_workout(training_max)
        else:
            errors = "training max must be a numeric value >= 112.5"
    return render(
        request,
        "home.html",
        {"workout": workout, "form": TrainingMaxForm(), "errors": errors},
    )
