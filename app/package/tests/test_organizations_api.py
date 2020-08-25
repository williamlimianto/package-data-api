from django.urls import reverse
from django.test import TestCase

from rest_framework import status

from core.models import Organization

from package.serializers import OrganizationSerializer


ORGANIZATIONS_URL = reverse('package:organization-list')


class OrganizationApiTest(TestCase):
    """Test the organization API"""

    def test_retrieve_organizations(self):
        """Test retrieving organizations"""
        Organization.objects.create(name='Organization A')

        res = self.client.get(ORGANIZATIONS_URL)

        organizations = Organization.objects.all().order_by('name')
        serializer = OrganizationSerializer(organizations, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_organization_successful(self):
        """Test creating a organization"""
        payload = {'name': 'Organization A'}
        self.client.post(ORGANIZATIONS_URL, payload)
        exists = Organization.objects.filter(
            name=payload['name']
        ).exists()
        self.assertTrue(exists)

    def test_create_organization_invalid(self):
        """Test creating a organization"""
        payload = {'name': ''}
        res = self.client.post(ORGANIZATIONS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
