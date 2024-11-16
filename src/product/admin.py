from django.contrib import admin

from src.product.models import Product


class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Product)
