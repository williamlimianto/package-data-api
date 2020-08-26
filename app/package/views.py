from rest_framework import viewsets, mixins

from core.models import Location, Organization, Customer

from package import serializers


class LocationViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """Manage locations in the database"""
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer

    def perform_create(self, serializer):
        """"Create a new location"""
        serializer.save()


class OrganizationViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin,
                          mixins.CreateModelMixin):
    """Manage organizations in the database"""
    queryset = Organization.objects.all()
    serializer_class = serializers.OrganizationSerializer

    def perform_create(self, serializer):
        """"Create a new organization"""
        serializer.save()


class CustomerViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """Manage customers in the database"""
    queryset = Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
