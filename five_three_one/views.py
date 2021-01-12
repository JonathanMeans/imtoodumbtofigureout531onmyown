from django.http import HttpResponse, response, HttpRequest
from django.shortcuts import render

from five_three_one.services import get_workout


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def workout_view(request: HttpRequest) -> HttpResponse:
    training_max = float(request.POST["tmax"])
    workout = get_workout(training_max)
    return render(request, "workout.html", {"workout": workout})
