from rest_framework import viewsets, mixins

from core.models import Location

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
