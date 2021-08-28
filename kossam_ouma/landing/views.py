from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "Home"}
    return render(request, "landing/home.html", context)


def about(request):
    return render(request, "landing/about.html", {"title": "About"})


def landing(request):
    return render(request, "index.html")
