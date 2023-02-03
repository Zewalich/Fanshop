from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from core.filtres.purchaser_filters import BalanceFilter
from core.permissions import IsOwnerOrReadOnly
from purchaser.api.v1.serializers.Balance_serializer import BalanceSerializer
from purchaser.models import Balance


class APIListPaginationPurchaser(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 15


class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    pagination_class = APIListPaginationPurchaser
    permission_classes = (IsOwnerOrReadOnly, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = BalanceFilter
    search_fields = ['value']
