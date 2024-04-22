# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class RegistrationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         labels = {
#             'username': "Ваше ім'я:",
#             'password': "Ваш пароль:"
#         }
#         widgets = {
#             'username': forms.TextInput(attrs={'type': "text", 'class': "form__input", 'placeholder': "МошьнийХакер2000"}),
#             'password': forms.TextInput(attrs={'type': "password", 'class': "form__input", 'placeholder': "31415926"}),
#         }

from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)