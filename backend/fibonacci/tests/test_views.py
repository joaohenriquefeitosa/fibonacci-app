import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

@pytest.mark.django_db
class TestFibonacciView:

    def setup_method(self):
        self.client = APIClient()
        self.base_url = 'http://localhost:8000/'
        self.app_name = 'fibonacci/'

    def test_fibonacci_valid_input(self):
        response = self.client.get(self.base_url + self.app_name, {'n': 5})
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {'result': [0, 1, 1, 2, 3]}

    def test_fibonacci_negative_input(self):
        response = self.client.get(self.base_url + self.app_name, {'n': -1})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'error': "'n' must be a non-negative integer."}

    def test_fibonacci_invalid_input(self):
        response = self.client.get(self.base_url + self.app_name, {'n': 'invalid'})
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'error': "'n' must be an integer."}

    def test_fibonacci_missing_input(self):
        response = self.client.get(self.base_url + self.app_name)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {'error': "'n' must be an integer."}
