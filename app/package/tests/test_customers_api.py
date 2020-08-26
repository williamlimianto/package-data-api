from django.urls import reverse
from django.test import TestCase

from rest_framework import status

from core.models import Customer, Location, Organization

from package.serializers import CustomerSerializer


CUSTOMERS_URL = reverse('package:customer-list')


def sample_organization(**params):
    """Create a sample organization"""
    defaults = {
        'name': 'Organization A'
    }
    defaults.update(params)

    return Organization.objects.create(**params)


def sample_location(**params):
    """Create a sample location"""
    defaults = {
        'name': 'Hub Jakarta Selatan',
        'code': 'JKTS01',
        'type': 'Agent'
    }
    defaults.update(params)

    return Location.objects.create(**params)


class CustomerApiTest(TestCase):
    """Test the customer API"""

    def test_retrieve_customers(self):
        """Test retrieving customers"""
        Customer.objects.create(customer_name='PT. NARA OKA PRAKARSA',
                                customer_address='JL. KH. AHMAD DAHLAN NO. 100'
                                                 ', SEMARANG TENGAH 12420',
                                customer_email='info@naraoka.co.id',
                                customer_phone="+62241234567",
                                customer_address_detail=None,
                                customer_zip_code="12420",
                                zone_code="CGKFT",
                                organization=sample_organization(),
                                location=sample_location())

        res = self.client.get(CUSTOMERS_URL)

        customers = Customer.objects.all().order_by('customer_name')
        serializer = CustomerSerializer(customers, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_customer_successful(self):
        """Test creating a customer"""
        organization = sample_organization()
        location = sample_location()
        payload = {'customer_name': 'PT. NARA OKA PRAKARSA',
                   'customer_address': 'JL. KH. AHMAD DAHLAN NO. 100'
                                       ', SEMARANG TENGAH 12420',
                   'customer_email': 'info@naraoka.co.id',
                   'customer_phone': '+62241234567',
                   'customer_address_detail': None,
                   'customer_zip_code': '12420',
                   'zone_code': 'CGKFT',
                   'organization_id': organization.id,
                   'location_id': location.id}

        res = self.client.post(CUSTOMERS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        customer = Customer.objects.get(customer_id=res.data['customer_id'])
        serializer = CustomerSerializer(customer)
        self.assertEqual(res.data, serializer.data)

    def test_create_customer_failed(self):
        """Test creating a customer with invalid parameter"""
        payload = {'customer_name': 'PT. NARA OKA PRAKARSA',
                   'customer_address': 'JL. KH. AHMAD DAHLAN NO. 100'
                                       ', SEMARANG TENGAH 12420',
                   'customer_email': 'info@@naraoka.co.id',
                   'customer_phone': '62241234567',
                   'customer_address_detail': None,
                   'customer_zip_code': '12420124201242012420',
                   'zone_code': 'CGKCGKFTCGKFTCGKFTFT',
                   'organization_id': None,
                   'location_id': None}

        res = self.client.post(CUSTOMERS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
