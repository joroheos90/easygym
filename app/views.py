from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, "hourselection.html")


def selector(request):
    return render(request, "hourselection.html")

def profile(request):
    return render(request, "profile.html")

def hours(request):
    return render(request, "hours.html")