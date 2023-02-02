from django.contrib import admin
from .models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    list_filter = ('category', 'price')
    list_display_links = ('name',)


class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)
