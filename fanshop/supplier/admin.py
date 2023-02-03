from django.contrib import admin

from supplier.models import Supplier, Founder


# Register your models here.
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'attribute', 'founding_date']
    ordering = ['-attribute']
    search_fields = ['name__istartwith']


@admin.register(Founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'age', 'fortune']
    ordering = ['-second_name']
    search_fields = ['second_name__istartwith']