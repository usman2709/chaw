from django.contrib import admin
from .models import Shopcart
from .models import Payment

# Register your models here.
@admin.register(Shopcart)
class ShopcartAdmin(admin.ModelAdmin):
    list_display = ['id','user','dish', 'c_name', 'c_date','quantity', 'c_price', 'amount', 'cart_code', 'paid']
    readonly_fields = ['user','dish', 'c_name', 'quantity','c_name', 'quantity','c_price','amount', ]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user','first_name', 'last_name', 'address','city' ,'total', 'cart_code', 'pay_code', 'pay_date', 'paid', 'admin_note', 'admin_update']
    readonly_fields = ['user','first_name', 'last_name', 'total', 'cart_code', 'pay_code', 'pay_date', 'paid',]