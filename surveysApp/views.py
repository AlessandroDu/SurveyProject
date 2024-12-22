from django.shortcuts import render


def home(request):
    return render(request, "surveysApp/home.html")


def index(request):
    return render(request, "surveysApp/index.html")
