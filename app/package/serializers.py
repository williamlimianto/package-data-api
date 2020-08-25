from rest_framework import serializers

from core.models import Location, Organization


class LocationSerializer(serializers.ModelSerializer):
    """Serializer for location objects"""

    class Meta:
        model = Location
        db_table = 'Location'
        fields = ('id', 'name', 'code', 'type', 'created_at',)
        read_only_fields = ('id', 'created_at',)


class OrganizationSerializer(serializers.ModelSerializer):
    """Serializer for organization objects"""

    class Meta:
        model = Organization
        db_table = 'Organization'
        fields = ('id', 'name',)
        read_only_fields = ('id',)
