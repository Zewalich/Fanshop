from rest_framework import viewsets



from core.permissions import IsAdminOrReadOnly
from fan_dealership.api.v1.serializers.Popularity_serializer import PopularitySerializer
from fan_dealership.api.v1.views.Fan_dealership_view import APIListPagination
from fan_dealership.models import Popularity


class PopularityViewSet(viewsets.ModelViewSet):
    queryset = Popularity.objects.all().order_by('value')
    serializer_class = PopularitySerializer
    pagination_class = APIListPagination
    permission_classes = (IsAdminOrReadOnly, )
    search_fields = ['value']