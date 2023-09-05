from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add test instances of the Menu model
        Menu.objects.create(title="Menu1", price=10, inventory=50, description="This is little lemon dish")
        Menu.objects.create(title="Menu2", price=15, inventory=30, description="This is little lemon dish")
        Menu.objects.create(title="Menu3", price=20, inventory=20, description="This is little lemon dish")

    def test_getall(self):
        # Get all Menu objects using the API
        client = APIClient()
        url = reverse('menu/')
        response = client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the serialized data equals the response data
        self.assertEqual(response.data, serializer.data)
