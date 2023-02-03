from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from core.filtres.fan_dealership_filters import AccessoriesFilter
from fan_dealership.api.v1.serializers.Accessories_serializer import AccessoriesSerializer
from fan_dealership.api.v1.views.Fan_dealership_view import APIListPagination
from fan_dealership.models import Accessories


class AccessoriesViewSet(viewsets.ModelViewSet):
    queryset = Accessories.objects.all().order_by('time_create')
    serializer_class = AccessoriesSerializer
    pagination_class = APIListPagination
    permission_classes = (AllowAny, )
    filter_backends = [DjangoFilterBackend]
    filterset_class = AccessoriesFilter
    search_fields = ['title', 'status']
    ordering_fields = ['title']