from django.urls import path
from .views import product

urlpatterns = [
    path('<str:id>/', product, name='product')
]
