from django.test import TestCase
from rest_framework.test import APITestCase

# Create your tests here.

from django.urls import reverse
from rest_framework import status

# from myproject.apps.core.models import Account

class HouseholdTests(APITestCase):

    def test_listing(self):
        """
        Ensure we can list all the households belonging to a user.
        """
        url = reverse('households.list')
        pass
  
    def test_listing_detail(self):
        """
        Ensure we can list all the households belonging to a user.
        """
        url = reverse('household.detail')
        pass

    def test_create_household(self):
        """
        Ensure we can create a new account object.
        """
        # url = reverse('')
        # data = {'name': 'DabApps'}
        # response = self.client.post(url, data, format='json')
        # self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # self.assertEqual(Account.objects.count(), s1)
        # self.assertEqual(Account.objects.get().name, 'DabApps')
        pass
