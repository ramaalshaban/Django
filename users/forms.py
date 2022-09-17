# im editing this page so i can edit the form 
from django import forms

import django_project
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# i will create form that inhernt from usercreationform

#  the thing inside the parentisic is the parent class
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
# config and namespace
    class Meta:
        model = User
        # here i will mention the model that i want the form to interact with
        # whenerver the form is validate it is going to create a new user 

        fields = ['username', 'email','password1', 'password2']

        # here is the field that are giong to be shown on our form 