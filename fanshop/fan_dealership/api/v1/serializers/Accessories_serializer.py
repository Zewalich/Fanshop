from rest_framework import serializers

from fan_dealership.models import Accessories

class AccessoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessories
        fields = ['title', 'price', 'currency', 'cat', 'status']