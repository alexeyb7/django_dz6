from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Client, Product, Order


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'address', 'client_reg_date')
    search_fields = ('name', 'email')
    list_filter = ('order__products', 'order__order_date')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'prod_name', 'prod_desc', 'prod_price', 'prod_quant', 'prod_reg_date')
    search_fields = ('prod_name', 'prod_desc')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'sum_order', 'order_date')
    search_fields = ('client__name', 'id')
    filter_horizontal = ('products',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
