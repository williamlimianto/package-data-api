from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Location

from package.serializers import LocationSerializer


LOCATIONS_URL = reverse('package:location-list')


class LocationsApiTets(TestCase):
    """Test the locations API"""

    def test_retrieve_locations(self):
        """Test retrieving locations"""
        Location.objects.create(name='Hub Jakarta Selatan', code='JKTS01', \
                                type='Agent')

        res = self.client.get(LOCATIONS_URL)

        locations = Location.objects.all().order_by('name')
        serializer = LocationSerializer(locations, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
