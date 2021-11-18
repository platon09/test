from django.contrib import admin

from market.models import *


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'shop')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', "name", "category", 'update_counter')
