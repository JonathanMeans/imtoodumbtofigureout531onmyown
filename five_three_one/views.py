from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from five_three_one.forms import TrainingMaxForm
from five_three_one.services import get_workout


def home_view(request: HttpRequest) -> HttpResponse:
    workout = None
    if request.method == "POST":
        training_max = float(request.POST["training_max"])
        workout = get_workout(training_max)
    return render(request, "home.html", {"workout": workout, "form": TrainingMaxForm()})
