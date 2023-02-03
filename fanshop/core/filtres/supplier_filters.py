from django_filters import rest_framework as filters

from supplier.models import Supplier, Founder


class SupplierFilter(filters.FilterSet):
    name = filters.CharFilter()

    class Meta:
        model = Supplier
        fields = ['name']


class FounderFilter(filters.FilterSet):
    first_name = filters.CharFilter()
    fortune = filters.RangeFilter()

    class Meta:
        model = Founder
        fields = ['first_name', 'fortune']
