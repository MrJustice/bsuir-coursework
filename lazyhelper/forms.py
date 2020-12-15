from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ['username', 'email', 'role', 'password1', 'password2']


class UserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields

        
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'comment', 'price']