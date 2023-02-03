from django.contrib import admin, messages
from django.db.models import QuerySet

from core.enums.fan_dealership_enums import Currency
from fan_dealership.models import Accessories, Fan_dealership, Popularity, Category


# Register your models here.
@admin.register(Accessories)
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'currency', 'cat']
    ordering = ['title']
    search_fields = ['title__istartwith']
    actions = ['change_to_eur', 'change_to_usd', 'change_to_rub']

    @admin.action(description='Изменить валюту выбранных элементов на евро')
    def change_to_eur(self, request, qs: QuerySet):
        updates_accessories = qs.update(currency=Currency.EUR)
        self.message_user(
            request,
            f'Обновлено {updates_accessories} записей',
            messages.INFO
        )

    @admin.action(description='Изменить валюту выбранных элементов на доллар')
    def change_to_usd(self, request, qs: QuerySet):
        updates_accessories = qs.update(currency=Currency.USD)
        self.message_user(
            request,
            f'Обновлено {updates_accessories} записей',
            messages.INFO
        )

    @admin.action(description='Изменить валюту выбранных элементов на рубль')
    def change_to_rub(self, request, qs: QuerySet):
        updates_accessories = qs.update(currency=Currency.RUB)
        self.message_user(
            request,
            f'Обновлено {updates_accessories} записей',
            messages.INFO
        )


@admin.register(Fan_dealership)
class Fan_dealershipAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']
    ordering = ['name']
    search_fields = ['name']


@admin.register(Popularity)
class PopularityAdmin(admin.ModelAdmin):
    list_display = ['accessor', 'value']
    ordering = ['value']
    search_fields = ['value']
    actions = ['change_to_popularity']

    @admin.action(description=' Изменить популярность у всех объектов на 5')
    def change_to_popularity(self, request, qs: QuerySet):
        updates_value = qs.update(value=5)
        self.message_user(
            request,
            f'Обновлено {updates_value} записей',
            messages.INFO
        )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']
    search_fields = ['name']
    actions = ['change_to_category']

    @admin.action(description=' Изменить категорию всех элементов на куртки')
    def change_to_category(self, request, qs: QuerySet):
        updates_accessories = qs.update(name='Куртки')
        self.message_user(
            request,
            f'Обновлено {updates_accessories} записей',
            messages.INFO
        )
