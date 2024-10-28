from django.shortcuts import render
from django.http import HttpRequest

def HomePage(request: HttpRequest):

    # return HttpResponse("Hello World")
    return render(request, "home.html")

def AboutPage(request: HttpRequest):
    # return HttpResponse("About Page")
    return render(request, "about.html")