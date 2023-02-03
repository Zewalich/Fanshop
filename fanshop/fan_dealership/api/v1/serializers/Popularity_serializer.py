from rest_framework import serializers

from fan_dealership.models import Popularity

class PopularitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Popularity
        fields = ['value', 'time_create']