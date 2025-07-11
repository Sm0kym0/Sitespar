from django.contrib import admin
from .models import Store

admin.site.register(Store)

from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_discounted')
    list_filter = ('category', 'is_discounted')
    search_fields = ('name',)
