from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from core.filtres.fan_dealership_filters import Fan_dealershipFilter

from fan_dealership.api.v1.serializers.Fan_dealership_serializer import Fan_dealershipSerializer
from fan_dealership.models import Fan_dealership


class APIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10


class Fan_dealershipViewSet(mixins.CreateModelMixin,
                            mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            mixins.ListModelMixin,
                            GenericViewSet):
    queryset = Fan_dealership.objects.all()
    serializer_class = Fan_dealershipSerializer
    pagination_class = APIListPagination
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [DjangoFilterBackend]
    filterset_class = Fan_dealershipFilter
    search_fields = ['name']
    ordering_fields = ['location']