# Import the forms library to create forms
from django import forms
from django.forms import ModelForm
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'nickname',
                  'email', 'password']

    first_name = forms.CharField()
    last_name = forms.CharField()
    nickname = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Confirm password")

