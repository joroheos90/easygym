from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    return render(request, "app/home.html")


def selector(request):
    return render(request, "app/hourselection.html")

def profile(request):
    return render(request, "app/profile.html")

def hours(request):
    return render(request, "app/hours.html")

def edit(request):
    return render(request, "app/editprofile.html")