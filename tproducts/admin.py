from django.contrib import admin
from .models import TProduct


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

admin.site.register(TProduct, ProductAdmin)