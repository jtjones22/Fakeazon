from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name="sign up"),
    path('signin/', views.signin, name="sign in"),
    path('signout/', views.signout, name="sign out"),
]