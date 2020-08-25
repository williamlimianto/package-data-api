from rest_framework import viewsets, mixins

from core.models import Location

from package import serializers

class LocationViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage locations in the database"""
    queryset = Location.objects.all()
    serializer_class = serializers.LocationSerializer
