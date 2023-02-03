from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filtres.supplier_filters import FounderFilter
from supplier.api.v1.serializers.Founder_serializer import FounderSerializer
from supplier.models import Founder


class APIListPaginationSupplier(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 15


class FounderViewSet(viewsets.ModelViewSet):
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
    pagination_class = APIListPaginationSupplier
    filter_backends = [DjangoFilterBackend]
    filterset_class = FounderFilter
    search_fields = ['first_name','second_name']
    oredering_fields = ['age']