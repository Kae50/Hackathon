from django.contrib.auth import authenticate,login
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

from ilearn.forms import SignupForms

# from ilearn.forms import SignupForms

# Create your views here.

class LandPageView(TemplateView):
    template_name = 'index.html'
class LoginView(TemplateView):
    template_name = 'registration/login.html'
# class SignUpView(TemplateView):
#     template_name = 'registration/signup.html'
#     model = SignupForms
class HomeView(TemplateView):
    template_name = 'home.html'

def SignUpView(request):
    if request.method == 'POST':
        form = SignupForms(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # email = form.cleaned_data.get('email')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username = username, raw_password=raw_password)
            login(request)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form':form})