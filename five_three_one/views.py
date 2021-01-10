from django.http import HttpResponse, response, HttpRequest
from django.shortcuts import render


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")
