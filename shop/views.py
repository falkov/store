from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Cart


class ProductList(ListView):
    """Список всех товаров"""
    model = Product
    template_name = 'shop/product-list.html'
    context_object_name = 'product_list'

    paginate_by = 3


class ProductDetail(DetailView):
    """Карточка товара"""
    model = Product
    # slug_field = 'slug'
    template_name = 'shop/product-detail.html'
    context_object_name = 'product'


class Cart(ListView):
    """ Корзина """
    model = Cart
    template_name = 'shop/cart.html'
    context_object_name = 'cart'


