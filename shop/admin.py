from django.contrib import admin
from .models import Product, CartItem, Order
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return "No Image"
    image_preview.short_description = "Preview"

admin.site.register(Product,ProductAdmin)
admin.site.register(CartItem)
admin.site.register(Order)


