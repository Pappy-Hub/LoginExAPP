# from django.contrib.auth.forms import ModelForm
from django import forms
from django.forms import ModelForm
# from django.contrib.auth.models import Business, Individual
from .models import Business, Individual
# from .models import User




class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'

        # fields = ['username', 'name', 'email', 'phoneNumber', 'referralCode', 'password']


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'

        fields = ['username', 'name', 'email', 'phoneNumber', 'referralCode', 'password']



# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'        