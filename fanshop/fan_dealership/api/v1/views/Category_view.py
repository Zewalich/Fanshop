from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticatedOrReadOnly

from fan_dealership.api.v1.serializers.Category_serializer import CategorySerializer
from fan_dealership.api.v1.views.Fan_dealership_view import APIListPagination
from fan_dealership.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
    pagination_class = APIListPagination
    search_fields = ['name']
