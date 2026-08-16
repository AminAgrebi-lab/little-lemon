# Import TestCase from Django's test module
from django.test import TestCase

# Import the Menu model from the restaurant app (Absolute import)
from restaurant.models import Menu

# Test case for the Menu model


class MenuTest(TestCase):
    # Test the string representation of the Menu model
    def test_get_item(self):
        # Create a new Menu instance in the test database
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)

        # Assert that the string representation matches the expected format
        self.assertEqual(str(item), "IceCream : 80")
