from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse 


# Create your views here.

def register(response):
    form = UserCreationForm()
    return render(response, "register/register.html", {"forms":form})

def view(request):
    return render(request, 'login.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'sign up.html')

def main(request):
    return render(request, 'main.html')

def table(request):
    return render(request, 'table.html')

def upload(request):
    return render(request, 'schedule.html')


