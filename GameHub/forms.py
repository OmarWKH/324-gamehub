from django import forms
from django.contrib.auth.forms import UserCreationForm
from registration.forms import RegistrationFormUniqueEmail
from .models import UserProfile

class LogInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserProfileRegistrationForm(RegistrationFormUniqueEmail):

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'username', 'country', 'email', 'password1', 'password2']
