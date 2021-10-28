from django.shortcuts import render, redirect
# from django.contrib.auth import authenticate, login as dj_login
from django.contrib import messages
from .models import Individual, Business
# from .models import User
# from .forms import IndividualForm, BusinessForm

# Create your views here.

def home(request):
    return render(request, 'index.html')

def get_started(request):  
    return render(request, 'getstarted.html')   
  


# def login(request):
          
#     return render(request, 'login.html')         
 


def learn(request):
    return render(request, 'learn.html') 
  

def instant_buy(request):
    return render(request, 'instantbuy.html')       
    #  return redirect ('/')


def dashboard(request):
   

    return render(request, 'dashboard.html')
  


def individual(request):
   

    return render(request, 'individual.html')
 



def business(request):
   
    return render(request, 'business.html')
     



def base(request):
    return render(request, 'base.html')       
    #  return redirect ('/')