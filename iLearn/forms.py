from django import forms
from django.contrib.auth.models import User


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields =[ 'username', 'email','password']
