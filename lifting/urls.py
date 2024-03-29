"""lifting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

import five_three_one.views

urlpatterns = [
    path("admin/", admin.site.urls),
    url(r"^$", five_three_one.views.home_view),
    url(r"^save$", five_three_one.views.save_exercise_view),
    url(r"^lifts$", five_three_one.views.lifts),
    url(r"^lift$", five_three_one.views.lift),
    url(r"^next_week$", five_three_one.views.next_week),
    url(r"^delete_lift$", five_three_one.views.delete_lift),
    url(r"^increase_tmax$", five_three_one.views.increase_tmax),
]
