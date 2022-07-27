from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('currency/', views.currency, name='currency'),
    path('fuel/', views.fuel, name='fuel'),
]
