from product.models import Product
from django.shortcuts import render

# Create your views here.


def catalog(request):
    products = Product.objects.all()
    countProducts = Product.objects.all().count()

    context = {'products': products, 'count': countProducts}
    return render(request, 'catalog.html', context)
