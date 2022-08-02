from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def home(requests):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories,
    }
    return render(requests, 'home.html', context)


def categories(requests, id):
    products = Product.objects.filter(category=id).values()
    context = {
        'products': products,
    }
    print(products)
    return render(requests, 'category.html', context)


def product(requests, id):
    context = {}
    return render(requests, 'product.html', context)
