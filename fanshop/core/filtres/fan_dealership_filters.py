from django_filters import rest_framework as filters

from core.enums.fan_dealership_enums import Currency
from fan_dealership.models import Accessories, Fan_dealership


class AccessoriesFilter(filters.FilterSet):
    price = filters.RangeFilter()
    currency = filters.ChoiceFilter(
        choices=Currency.choices,
    )
    year = filters.RangeFilter()

    class Meta:
        model = Accessories
        fields = ['price', 'currency', 'year']


class Fan_dealershipFilter(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Fan_dealership
        fields = ['name', 'location']
