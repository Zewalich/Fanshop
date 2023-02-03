from django.contrib import admin

from purchaser.models import Purchaser, Balance


# Register your models here.
@admin.register(Purchaser)
class PurchaserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'sex', 'phone']
    ordering = ['-first_name']
    search_fields = ['first_name']


@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ['purch', 'value']
    ordering = ['-purch']
    search_fields = ['value']