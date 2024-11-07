from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.

def Register(request: HttpRequest):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("posts:list")
    else: 
        form = UserCreationForm()
    return render(request, "auth/register.html", {"form": form})

def Login(request: HttpRequest):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, "auth/login.html", {"form": form})
