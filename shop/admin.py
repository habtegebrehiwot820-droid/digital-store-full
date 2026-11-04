from django.contrib import admin
from .models import DigitalProduct

@admin.register(DigitalProduct)
class DigitalProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'supplier_name')
    search_fields = ('title', 'supplier_name')