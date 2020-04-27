from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import Product
from .models import Size
from .models import CartItem
from .models import Cart
from django.template import loader
from django.views.generic import ListView, DetailView, View, CreateView, FormView, TemplateView
import sys
import logging
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


class OwnerPage(TemplateView):
    template_name = 'owner.html'
    # def get(self, request, *args, **kwargs):
    #     return HttpResponse('owner.html')


class AddForm(LoginRequiredMixin, CreateView):
    login_url = '/testStore/login/'
    model = Product
    fields = [
        'name',
        'price',
        'photo1',
        'photo2',
        'slug'
    ]


class AddSize(LoginRequiredMixin, CreateView):
    login_url = '/testStore/login/'
    model = Size
    fields = [
        'product',
        'size',
        'price',
        'qty',
        'in_stock'
    ]


class ProductView(DetailView):
    model = Product
    template_name = "productPage.html"


class HomeView(ListView):
    model = Product
    template_name = "storeFront.html"


class CartView(View):
    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(session=self.request.session.session_key)
            context = {
                'object': cart
            }
            return render(self.request, 'cart.html', context)
        except ObjectDoesNotExist:
            return render(self.request, "cart.html")


class OrderForm(View):
    def get(self, *args, **kwargs):
        try:
            cart = Cart.objects.get(session=self.request.session.session_key)
            context = {
                'object': cart
            }
            return render(self.request, 'orderForm.html', context)
        except ObjectDoesNotExist:
            return render(self.request, "orderForm.html")


def add_to_cart(request, slug):
    if not request.session.exists(request.session.session_key):
        request.session.create()

    request.session.save()
    session_id = request.session.session_key
    new_item = get_object_or_404(Product, slug=slug)
    size = ''
    qty = int
    if request.method == "POST":
        for item in request.POST:
            if item == 'qty':
                key = item
                qty = int(request.POST[key])
                print(qty, type(qty), flush=True)
            elif item == 'size':
                key = item
                print(key, flush=True)
                item_size = request.POST[key]
                print(item_size, flush=True)
                if Size.objects.filter(size=item_size, product=new_item).exists():
                    size_object = Size.objects.filter(size=item_size, product=new_item)
                    size = size_object[0]

    cart_item, created = CartItem.objects.get_or_create(item=new_item, size=size, session=session_id)
    cart_qs = Cart.objects.filter(session=session_id)
    print(request.session.session_key, flush=True)

    if cart_qs.exists():
        cart = cart_qs[0]
        item_qs = cart.item.filter(item=cart_item.item)
        if item_qs.exists():
            for item in item_qs:
                if item.size == size:
                    cart_item.qty += qty
                    cart.item.add(cart_item)
                    cart_item.save()
                else:
                    cart_item.qty = qty
                    cart.item.add(cart_item)
                    cart_item.save()
        else:
            cart_item.qty = qty
            cart_item.save()
            cart.item.add(cart_item)
    else:
        cart = Cart.objects.create(session=request.session.session_key)
        cart_item.qty = qty
        cart_item.save()
        cart.item.add(cart_item)
        cart.save()
    messages.success(request, 'Item Added to Cart!')
    return redirect("product", slug=slug)


def remove_from_cart(request, id):
    request.session.save()
    item = CartItem.objects.get(id=id)

    item.delete()
    return redirect("cart")
