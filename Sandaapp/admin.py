from django.contrib import admin

from .models import Customer, Product, Order, Cart, OrderDetail, Favorite, Addresses, Payment


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_id', 'cust_firstname', 'cust_lastname', 'phone_number')
    list_filter = ('cust_id', 'cust_firstname')
    search_fields = ('cust_id',)
    ordering = ['cust_id']


class ProductList(admin.ModelAdmin):
    list_display = ('product_id', 'product_name', 'product_price')
    list_filter = ('product_id', 'product_name')
    search_fields = ('product_name',)
    ordering = ['product_name']


admin.site.register(Customer, CustomerList)
admin.site.register(Product, ProductList)
admin.site.register(Order)
admin.site.register(Payment)
admin.site.register(Addresses)
admin.site.register(Favorite)
admin.site.register(OrderDetail)
admin.site.register(Cart)

