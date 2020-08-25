from django.urls import reverse
from django.test import TestCase

from rest_framework import status

from core.models import Location

from package.serializers import LocationSerializer


LOCATIONS_URL = reverse('package:location-list')


class LocationsApiTest(TestCase):
    """Test the locations API"""

    def test_retrieve_locations(self):
        """Test retrieving locations"""
        Location.objects.create(name='Hub Jakarta Selatan', code='JKTS01',
                                type='Agent')

        res = self.client.get(LOCATIONS_URL)

        locations = Location.objects.all().order_by('name')
        serializer = LocationSerializer(locations, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_location_successful(self):
        """Test creating a location"""
        payload = {'name': 'Hub Jakarta Selatan',
                   'code': 'JKTS01',
                   'type': 'Agent'}
        self.client.post(LOCATIONS_URL, payload)
        exists = Location.objects.filter(
            name=payload['name'],
            code=payload['code'],
            type=payload['type']
        ).exists()
        self.assertTrue(exists)

    def test_create_location_invalid(self):
        """Test creating a location"""
        payload = {'name': '',
                   'code': 'Hub Jakarta SelatanHub Jakarta Selatan Selatan',
                   'type': 'AgentAgentAgentAgentAgent'}
        res = self.client.post(LOCATIONS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
