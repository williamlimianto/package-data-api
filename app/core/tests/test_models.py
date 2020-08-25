from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


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
