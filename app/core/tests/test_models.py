from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_organization(name='Organization A'):
    """Create a sample organization"""
    return models.Organization.objects.create(name=name)


def sample_location(name='Hub Jakarta Selatan', code='JKTS01', type='Agent'):
    """Create a sample location"""
    return models.Location.objects.create(name=name, code=code, type=type)


class ModelTests(TestCase):

    def test_create_user(self):
        """Test creating a new user with an email is successfull"""
        username = 'test'
        password = 'password123'
        name = 'Test user full name'
        user = get_user_model().objects.create_user(
            username=username,
            password=password,
            name=name
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.name, name)

    def test_create_superuser(self):
        """Test creating a new superuser"""
        username = 'admin'
        password = 'password123'
        user = get_user_model().objects.create_superuser(
            username=username,
            password=password,
        )

        self.assertEqual(user.username, username)
        self.assertTrue(user.check_password(password))

    def test_location_str(self):
        """Test the location string representation"""
        location = models.Location.objects.create(
            name='Hub Jakarta Selatan',
            code='JKTS01',
            type='Agent'
        )

        self.assertEqual(str(location), location.name)

    def test_organization_str(self):
        """Test the organization string representation"""
        organization = models.Organization.objects.create(
            name='Organization A'
        )

        self.assertEqual(str(organization), organization.name)

    def test_customer_str(self):
        """Test the customer string representation"""
        customer = models.Customer.objects.create(
            customer_name='PT. NARA OKA PRAKARSA',
            customer_address='JL. KH. AHMAD DAHLAN NO. 100, SEMARANG '
                             'TENGAH 12420',
            customer_email='info@naraoka.co.id',
            customer_phone="024-1234567",
            customer_address_detail=None,
            customer_zip_code="12420",
            zone_code="CGKFT",
            organization=sample_organization(),
            location=sample_location()
        )

        self.assertEqual(str(customer), customer.customer_name)
