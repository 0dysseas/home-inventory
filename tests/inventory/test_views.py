import pytest
# import pytest_django
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class TestInventoryList(APITestCase):
    @pytest.mark.django_db
    def test_get_product_list(self):
        url = reverse('product-list')
        response = self.client.get(url)
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 9)