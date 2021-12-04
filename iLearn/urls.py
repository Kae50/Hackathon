from django.urls import path
from .import views

urlpatterns = [
    path('', views.LandPageView.as_view(), name='index'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('search/',views.resultView.as_view(),name='result'),
    path('learn/',views.numberView.as_view(),name='learn'),
]