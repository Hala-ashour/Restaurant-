from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .model import Customer

class CustomerAPITest(APITestCase):

    def setUp(self):
        self.customer_data = {
            'name': 'Bayan',
            'email': 'bayan@example.com',
            'phone_number': '1234567890',
            'address': 'Damascus'
        }
        self.url = reverse('customer-list')  

    def test_create_customer(self):
        response = self.client.post(self.url, self.customer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_customers(self):
        Customer.objects.create(**self.customer_data)
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
