from pyexpat import model
from statistics import mode
from django.forms import modelformset_factory
from django.shortcuts import render
from .models import Product

# Create your views here.


def product(request, id):
    product = Product.objects.get(id=id)
    context = {'id': id, 'product': product}
    return render(request, 'product.html', context)
