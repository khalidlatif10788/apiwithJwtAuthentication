

# vim: set fileencoding=utf-8 :
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class pcategoryAdmin(admin.ModelAdmin):

    list_display = ('id', 'c_name', 'c_description', 'thumbnail')
    list_filter = ('id', 'c_name', 'c_description', 'thumbnail')


class brandAdmin(admin.ModelAdmin):

    list_display = ('id', 'b_name', 'b_description', 'thumbnail')
    list_filter = ('id', 'b_name', 'b_description', 'thumbnail')
class productAdmin(admin.ModelAdmin):

    list_display = (
        
        'id',
        'pname',
        'pdescription',
        'psalep',
        'pdiscountp',
        'psize',
        'product_stock',
        'product_creation_date',
        'photo',
        'P_brand',
        'pcate',
       
        
    )
    list_filter = (
        'product_creation_date',
        'id',
        'pname',
        'pdescription',
        'psalep',
        'pdiscountp',
        'psize',
        'product_stock',
        'product_creation_date',
       
       
    )
  







class customerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customer',
        'phone',
        'billing_address',
        'shipping_address',
        'country',
    )
    list_filter = (
        'customer',
        'id',
        'customer',
        'phone',
        'billing_address',
        'shipping_address',
        'country',
    )


class cartAdmin(admin.ModelAdmin):

    list_display = ('id', 'customer', 'prd', 'qty', 'totalAmount')
    list_filter = (
        'customer',
        'prd',
        'id',
        'customer',
        'prd',
        'qty',
        'totalAmount',
    )


class orderAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'customerid',
        'amount',
        'order_address',
        'shipping_address',
        'order_email',
        'orderdate',
        'order_status',
    )
    list_filter = (
        'customerid',
        'orderdate',
        'id',
        'customerid',
        'amount',
        'order_address',
        'shipping_address',
        'order_email',
        'orderdate',
        'order_status',
    )


class order_detailAdmin(admin.ModelAdmin):

    list_display = ('id', 'order_id', 'product_id', 'qty', 'price')
    list_filter = (
        'order_id',
        'product_id',
        'id',
        'order_id',
        'product_id',
        'qty',
        'price',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.pcategory, pcategoryAdmin)
_register(models.brand, brandAdmin)
_register(models.product, productAdmin)

_register(models.cart, cartAdmin)
_register(models.order, orderAdmin)
_register(models.order_detail, order_detailAdmin)
_register(models.customer, customerAdmin)
