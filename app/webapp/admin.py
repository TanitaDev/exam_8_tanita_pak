from django.contrib import admin

from webapp.models import Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'image']


class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'product', 'rate', 'text']


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
