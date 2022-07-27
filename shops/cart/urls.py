from django.urls import path
from .views import cart


urlpatterns = [
    path('<str:id>', cart, name='cart'),
]
