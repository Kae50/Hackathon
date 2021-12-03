from typing import Optional
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignupForms(UserCreationForm):
    username = forms.CharField(max_length=200, required=True,)
    email = forms.EmailField(max_length=200, required=True)
    password = forms.CharField(max_length = 240) 

    def __init__(self,*args,**kwargs):
        super(UserCreationForm,self).__init__(*args, **kwargs)
        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None
    # class Meta:
    #     model = User
    #     fields =('username','email','password')