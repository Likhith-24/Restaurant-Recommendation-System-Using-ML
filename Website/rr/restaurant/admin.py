from django.contrib import admin

# Register your models here.
from .models import *

class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ("user","order_id",'order_date')


admin.site.register(OrderPlaced,OrderPlacedAdmin)