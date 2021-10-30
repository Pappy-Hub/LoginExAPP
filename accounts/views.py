from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    return render(request, 'accounts/register.html')
    
def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return redirect ('index')   


def dashbaord(request):
    return render(request, 'accounts/dashboard.html')     

# def welcome(request):
#     return render (request, 'accounts/welcome.html')  