from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product


class ProductList(ListView):
    """Список всех товаров"""
    model = Product
    template_name = 'shop/list-product.html'


class ProductDetail(DetailView):
    """Карточка товара"""
    model = Product
    slug_field = 'slug'
    template_name = 'shop/detail-product.html'

    # queryset = Product.objects.filter(slug='slug')
