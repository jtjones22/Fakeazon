from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('product/<str:pk>/', views.product, name='product'),
    path('company/<str:pk>/', views.company, name='company'),
    path('create_company/', views.create_company, name='create company'),
    path('update_company/<str:pk>', views.update_company, name='update company'),
    path('create_product/', views.create_product, name='create product'),
    path('update_product/<str:pk>', views.update_product, name='update product'),
]
    
