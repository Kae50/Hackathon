from django.urls import path
from .import views

urlpatterns = [
    path('', views.LandPageView.as_view(), name='index'),
    path('registration/login/', views.LoginView.as_view(), name='login'),
    # path('accounts/l/', views.LandPageView.as_view(), name='logout'),
    path('registration/signup/', views.SignUpView, name='signup'),
    path('home/', views.HomeView.as_view(), name='home'),
]