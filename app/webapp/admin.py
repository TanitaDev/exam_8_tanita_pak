from django.contrib import admin

from webapp.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']


admin.site.register(Product)
