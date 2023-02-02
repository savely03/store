from .models import Order, OrderItem, ConfirmOrder
from django.contrib import admin


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "first_name", "last_name", "email", "address", "created_date", "updated_date"]
    list_filter = ['confirm', 'created_date', 'updated_date']


class ConfirmOrderAdmin(admin.ModelAdmin):
    list_display = ["user", "id", "first_name", "last_name", "email", "address", "created_date", "updated_date"]
    list_filter = ["status", 'created_date', 'updated_date']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(ConfirmOrder, ConfirmOrderAdmin)
