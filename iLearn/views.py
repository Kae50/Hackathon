from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView
from .models import Word, Number
from django.db.models import Q
from . import forms
from .forms import SignUpForm
from django.contrib.auth import authenticate,login

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()   
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password=password)
            login(request, user)
            return redirect('home', user)
    else:
        form = SignUpForm()   

    return render(request, 'signup.html',{'form':form})

def Login(request):
    if request.method == 'GET':
        # form = forms.SignUpForm(request.GET)
        # if form.is_valid(): 
        #     username = form.cleaned_data.get('username')
        #     password = form.cleaned_data.get('password')
            # user = authenticate()
            # login(request)
            return redirect('home')

    return render(request, 'signup.html')

class LandPageView(TemplateView):
    template_name = 'index.html'

# def Login(request):
#     return render(request, 'login.html')
    

class HomeView(TemplateView):
    template_name = 'home.html'

class resultView(ListView):
    template_name = 'result.html'
    model = Word

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        object_list = Word.objects.filter(
            Q(word__icontains= query) | Q(translation__icontains= query)
            )

        return object_list

class numberView(ListView):
    template_name = 'learn.html'
    model = Number

    def get_queryset(self):
        query = self.request.GET.get('keyword')
        object_list = Number.objects.all()

        return object_list

