from django.shortcuts import render, redirect
#<<<<<<< HEAD
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.http import HttpResponse 


# Create your views here.

def register(response):
    if response.method == "POST":
        #form = UserCreationForm(response.POST)
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form":form})

def view(request):
    return render(request, 'login.html')


