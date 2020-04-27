from djmoney.models.fields import MoneyField
from django.db import models


# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    inventory = models.IntegerField(default=0)
    photo1 = models.ImageField(upload_to='media/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='media/', blank=True, null=True)

    def __str__(self):
        return self.product_name
