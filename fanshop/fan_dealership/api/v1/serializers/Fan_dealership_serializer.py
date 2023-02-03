from rest_framework import serializers

from fan_dealership.models import Fan_dealership

class Fan_dealershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fan_dealership
        fields = ['name', 'location', 'contact']