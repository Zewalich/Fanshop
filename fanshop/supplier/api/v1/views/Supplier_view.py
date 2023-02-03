from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from core.filtres.supplier_filters import SupplierFilter
from supplier.api.v1.serializers.Supplier_serializer import SupplierSerializer
from supplier.api.v1.views.Founder_view import APIListPaginationSupplier
from supplier.models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all().order_by('name')
    serializer_class = SupplierSerializer
    pagination_class = APIListPaginationSupplier
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    search_fields = ['name']
    oredering_fields = ['location']