
from django.urls import path
from shop.views import home, product

urlpatterns = [
    path('', home, name='home'),
    path('product/<str:id>', product, name='product')

]
