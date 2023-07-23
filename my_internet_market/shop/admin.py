from django.contrib import admin
from .models import Shop, Brand, Product

class ShopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'addres', 'products', )
    list_display_links = ('name', 'addres', )
    search_fields = ('name', 'addres', )
    #prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'content', 'price', 'shipment', 'multiple', )

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_shop', )

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Brand)


