from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
name = "Sudh"


def blog(request):
    global name
    return render(request, "blog1.html", {'name': name})


def add(request):
    return render(request, "result.html")
