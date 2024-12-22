from django.shortcuts import render

from .models import Questions


def home(request):
    return render(request, "surveysApp/home.html")


def index(request):
    questions = Questions.objects.get(pk=1)
    return render(request, "surveysApp/index.html", {"questions": questions})
