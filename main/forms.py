from django.contrib.auth.forms import AuthenticationForm
from django import forms

# from .models import Donate, Post

class UserLogin(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'Name', 'placeholder': 'Вводите логин', 'class': 'formimput', }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'type': 'Password', 'placeholder': 'Вводите пароль', 'class': 'formimput', }))

