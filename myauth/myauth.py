from django import forms
from django.form import PasswordInput

class login_form(forms, Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=PasswordInput)