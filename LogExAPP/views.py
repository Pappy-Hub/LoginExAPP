from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as dj_login
from django.contrib import messages
from .models import Business
# from .models import User
# from .forms import IndividualForm, BusinessForm

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

# def get_started(request):  
#     return render(request, 'getstarted.html')   
  


# def login(request):          
#     return render(request, 'login.html')         
 


def learn(request):
    return render(request, 'pages/learn.html') 
  

def instant_buy(request):
    return render(request, 'pages/instantbuy.html')       
    #  return redirect ('/')


def dashboard(request): 
    return render(request, 'dashboard.html')
  


def individual(request):
    return render(request, 'pages/individual.html')
 



def business(request):   
    return render(request, 'pages/business.html')
     



def welcome(request):
    return render(request, 'pages/welcome.html')    