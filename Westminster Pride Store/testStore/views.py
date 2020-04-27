from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from django.template import loader
from django.shortcuts import render

# Create your views here.

def index(request):
    product_list = Product.objects.all()
    context = {
        'product_list': product_list,
    }
    return render(request, 'storeFront.html', context)


def product(request, id):
    show_product = get_object_or_404(Product, pk=id)
    context = {
        'product': show_product,

    }
    return render(request, 'productPage.html', context)
