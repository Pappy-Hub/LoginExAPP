from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate
from LogExAPP.models import Business

# Create your views here.
def register(request):
    #  global username, password, email
     if request.method == 'POST':
         fullname = request.POST['fullname']
         username = request.POST['username']
         email = request.POST['email']
         phonenumber = request.POST['phonenumber']
         password = request.POST['password'] 
         password2 = request.POST['password2']
         
         # Check if passwords match
         if password == password2:
            # Check username
             if User.objects.filter(username=username).exists():
                 messages.error(request, 'That username is taken')
                 return redirect('register')
             else:    
                if User.objects.filter(email=email).exists():
                 messages.error(request, 'That email is being used')
                 return redirect('register')
                else:
                 #Looks good                         
                 user = User.objects.create_user(username=username, password=password, email=email)

                #  Login after register alternative
                #  auth.login(request, user)
                #  messages.success(request, 'You are now logged in')
                #  return redirect('index')

                 user.save();
                 messages.success(request, 'You are now registered and can log in')
                 return redirect('register')                 
               
         else:                  
            messages.error(request, 'password do not match') 
            return redirect('register')         
                                   

    #     messages.error(request, 'Testing Error Message')
    #     # print('Submitted Reg')
    #     return redirect ('register')
     else:
         return render(request, 'accounts/register.html')
            
    
    
def login(request):  
     if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'you are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credencials')
            return redirect('login')
      
     else:
        return render(request, 'accounts/login.html')

def logout(request):
     if request.method == 'POST':
          auth.logout(request)
          messages.error(request, 'You are now logged out')
          return redirect('index')
     


def dashbaord(request):
    return render(request, 'accounts/dashboard.html')     

# def welcome(request):
#     return render (request, 'accounts/welcome.html')  






# def login(request):  
#      if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 dj_login(request, user)
#                 return redirect('index')

#             else:
#                 return redirect('login')
#         else:
#             return redirect('index')  

#      return render(request, 'accounts/login.html')                
