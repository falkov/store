from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, Product
from .models import Cart, CartItem, Order


class CategoryMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20  # specify pixel amount for this ModelAdmin only:

admin.site.register(Category, CategoryMPTTModelAdmin)

admin.site.register(Product)

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
