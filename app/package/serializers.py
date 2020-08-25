from rest_framework import serializers

from core.models import Location


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for location objects"""

    class Meta:
        model = Location
        fields = ('id', 'name', 'code', 'type', 'created_at')
        read_only_fields = ('id', 'created_at')
