from rest_framework import serializers

from core.models import Location, Organization, Customer


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
        read_only_fields = ('id', 'created_at',)


class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for customer objects"""
    organization_id = serializers.PrimaryKeyRelatedField(
        source='organization',
        many=False,
        queryset=Organization.objects.all()
    )
    location_id = serializers.PrimaryKeyRelatedField(
        source='location',
        many=False,
        queryset=Location.objects.all()
    )

    class Meta:
        model = Customer
        db_table = 'Customer'
        fields = ('customer_id', 'customer_name', 'customer_address',
                  'customer_email', 'customer_phone',
                  'customer_address_detail',
                  'customer_zip_code', 'zone_code', 'organization_id',
                  'location_id')
        read_only_fields = ('customer_id', 'created_at',)
