from django.tests import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_menu_item(self):
        item = Menu.objects.create(title='Pasta', price='20', inventory=100)
        self.assertEqual(item, 'Pasta : 20')