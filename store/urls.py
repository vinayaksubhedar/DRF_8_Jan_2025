"""storefront URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('products', views.products, name='products'),
    path('products/coffe', views.products_cofee, name='products_cofee'),
    path('products/<int:year>', views.products_year, name='products_year'),
    path('top_orders', views.top_orders, name='top_orders'),
    path('product_collection', views.product_collection, name='product_collection'),
    path('collections', views.collections, name='collections'),
    path('product_api/', views.product_api, name='product_api'),
]
