from typing import Optional

from django.forms.utils import ErrorDict
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from five_three_one.forms import TrainingMaxForm, NewLiftForm
from five_three_one.models import Lift
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
        {
            "workout": workout,
            "form": TrainingMaxForm(),
            "errors": errors,
            "new_lift_form": NewLiftForm(),
        },
    )


def save_exercise_view(request: HttpRequest) -> HttpResponse:
    form = NewLiftForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect("/lifts")


def lifts(request: HttpRequest) -> HttpResponse:
    all_lifts = Lift.objects.all()
    return render(request, "lifts.html", {"lifts": all_lifts})


def lift(request: HttpRequest) -> HttpResponse:
    tmax_form = TrainingMaxForm(request.GET)
    workout = None
    if tmax_form.is_valid():
        training_max = float(request.GET["training_max"])
        week_number = int(request.GET["week_number"])
        workout = get_workout(training_max, week_number)

    return render(
        request,
        "lift.html",
        {
            "workout": workout,
        },
    )
