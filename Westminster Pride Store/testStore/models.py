from djmoney.models.fields import MoneyField
from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from importlib import import_module
from django.contrib.sessions.backends.db import SessionStore


# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    photo1 = models.ImageField(upload_to='media/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='media/', blank=True, null=True)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })


class Size(models.Model):
    Size_Choice = [
        ('XS', 'XS'),
        ('SM', 'SM'),
        ('MD', 'MD'),
        ('LG', 'LG'),
        ('XL', 'XL'),
        ('2XL', '2XL'),
        ('3XL', '3XL'),
        ('4XL', '4XL')
    ]
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=4, null=True, choices=Size_Choice)
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    qty = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.size}"

    def get_absolute_url(self):
        return reverse("product", kwargs={
            'slug': self.product.slug
        })


class CartItem(models.Model):
    session = models.CharField(max_length=200, null=True, default='noSessionID')
    item = models.ForeignKey(Product, on_delete=models.CASCADE, null=False)
    size = models.ForeignKey(Size, on_delete=models.CASCADE, null=True)
    qty = models.IntegerField(default=1, null=False)

    def total_price(self):
        return self.qty * self.size.price

    def __str__(self):
        return f"{self.qty} of {self.item} size {self.size} "


class Cart(models.Model):
    session = models.CharField(max_length=200, null=True, default='noSessionID')
    item = models.ManyToManyField(CartItem)
    slug = models.SlugField(null=False)

    def order_total(self):
        total = 0
        for item in self.item.all():
            total += item.total_price()
        return total

    def __str__(self):
        return f"{self.id} "
