from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect

from five_three_one.forms import NewLiftForm
from five_three_one.models import Lift
from five_three_one.services import get_workout


def home_view(request: HttpRequest) -> HttpResponse:
    all_lifts = Lift.objects.all()
    return render(
        request,
        "home.html",
        {
            "form": NewLiftForm(),
            "lifts": all_lifts,
        },
    )


def save_exercise_view(request: HttpRequest) -> HttpResponse:
    form = NewLiftForm(request.POST)
    if form.is_valid():
        saved_lift = form.save()
        return redirect(saved_lift.url)
    else:
        return render(
            request,
            "home.html",
            {
                "errors": form.errors,
                "form": NewLiftForm(),
                "lifts": Lift.objects.all(),
            },
        )


def lifts(request: HttpRequest) -> HttpResponse:
    all_lifts = Lift.objects.all()
    return render(request, "lifts.html", {"lifts": all_lifts})


def lift(request: HttpRequest) -> HttpResponse:
    lift_id = request.GET["id"]
    the_lift = Lift.objects.get(id=lift_id)
    workout = get_workout(the_lift.training_max, the_lift.week_number)
    return render(
        request,
        "lift.html",
        {
            "workout": workout,
            "lift": the_lift,
        },
    )


def delete_lift(request: HttpRequest) -> HttpResponse:
    lift_id = request.GET["id"]
    the_lift = Lift.objects.get(id=lift_id)
    the_lift.delete()
    return redirect("/lifts")


def next_week(request: HttpRequest) -> HttpResponse:
    lift_id = request.GET["id"]
    the_lift = Lift.objects.get(id=lift_id)
    the_lift.week_number = (the_lift.week_number % 3) + 1
    the_lift.save(update_fields=["week_number"])
    return redirect(the_lift.url)
