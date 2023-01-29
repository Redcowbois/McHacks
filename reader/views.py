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


