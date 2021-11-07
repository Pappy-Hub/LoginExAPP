from django.db import models
# from django.contrib.auth.models import AbstractUser

# from LogExAPP.views import business, individual


# Create your models here.

class Business(models.Model):
     username = models.CharField(max_length=20, unique=True)
     fullname = models.CharField(max_length=50)
     email = models.EmailField(('email address'), unique=True)
     phonenumber = models.IntegerField(default=0)
     referral_code = models.CharField(max_length=8, default='Optional')
      

     def __str__(self):
         return self.username


# class Individual(models.Model):
#      username = models.CharField(max_length=100)
#      name = models.CharField(max_length=100, default='new')
#      email = models.EmailField(max_length=100, default='new')
#      phoneNumber = models.IntegerField(default=1)
#      referralCode = models.CharField(max_length=8, default='new')
#      password = models.CharField(max_length=50, default='new')
   

#      def __str__(self):
#          return self.username


# class User(models.Model):
#      business = models.CharField(max_length=20, blank=True, null=True)
#      individual = models.CharField(max_length=20, blank=True, null=True)
#      fullname = models.CharField(max_length=50)  
#      phonenumber = models.IntegerField(default=1)
#      referralCode = models.CharField(max_length=8, blank=True, null=True)
 
   
       