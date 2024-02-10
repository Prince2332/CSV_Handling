from django.shortcuts import render
import csv

# Create your views here.


def login(request):
    return render(request, "base.html")


def csv_file(request):
    return render(request, "validation.html")


def csv_validator(request):
    if request.method == "POST":
        if "file" in request.FILES:
            file = request.FILES["file"]
            for line in file.read().decode("utf-8").splitlines():
                # Assuming the file contains a CSV and you want to process it as CSV data
                row = line.split(",")
                print(row[0], row[1])
    return render(request, "validation.html")
