from django.contrib import admin
from .models import Product
from .models import CartItem
from .models import Cart
from .models import Size

# Register your models here.
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Cart)
admin.site.register(Size)
