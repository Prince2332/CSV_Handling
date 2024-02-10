from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("validation", views.csv_file, name="validation page"),
    path("csv_validator", views.csv_validator, name="csv_validator"),
]
