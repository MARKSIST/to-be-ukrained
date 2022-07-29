from django import views
from django.urls import path
from shop.views import main

urlpatterns = [
    path('', main, name='main')
]
