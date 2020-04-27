
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from testStore import views
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.shortcuts import render, get_object_or_404, redirect, reverse

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('testStore/', include('django.contrib.auth.urls')),  # new
    path('testStore/product<slug>/', views.ProductView.as_view(), name='product'),
    path('testStore/add_to_cart<slug>/', views.add_to_cart, name='add_to_cart'),
    path('testStore/remove_from_cart<id>/', views.remove_from_cart, name='remove_from_cart'),
    path('testStore/cart/', views.CartView.as_view(), name='cart'),
    path('testStore/checkout/', views.OrderForm.as_view(), name='checkout'),
    path('add_form/', views.AddForm.as_view(), name='add_prod'),
    path('size_form/', views.AddSize.as_view(), name='add_size'),
    path('admin/', admin.site.urls),
    path('owner/', views.OwnerPage.as_view(), name='owner'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


