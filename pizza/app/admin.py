from django.contrib import admin
from .models import *

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'full_name', 'address', 'phone_number')
    search_fields = ('username', 'email', 'full_name')
    ordering = ('username',)
    readonly_fields = ('password',)  

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    search_fields = ('category_name',)
    ordering = ('category_name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'category')
    search_fields = ('product_name', 'category__category_name')
    list_filter = ('category',)
    ordering = ('product_name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'product', 'quantity')
    search_fields = ('session_key', 'product__product_name')
    list_filter = ('product',)
    ordering = ('session_key',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'quantity', 'status', 'address')
    search_fields = ('user__username', 'status', 'address')
    list_filter = ('status', 'order_date')
    ordering = ('-order_date',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__product_name')
    list_filter = ('order', 'product')
    ordering = ('order', 'product')
