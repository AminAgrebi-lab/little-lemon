# Import necessary modules for testing API views
from django.test import TestCase
from rest_framework.test import APIClient

# Import the Menu model and its serializer using absolute imports
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

# Test case for the Menu API views


class MenuViewTest(TestCase):
    # Set up test data before each test method runs
    def setUp(self):
        # Add test instances of the Menu model to the test database
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

    # Test retrieving all menu items via the API endpoint
    def test_getall(self):
        # Retrieve all Menu objects from the database
        items = Menu.objects.all()

        # Serialize the retrieved objects
        serializer = MenuSerializer(items, many=True)

        # Initialize the API client and send a GET request to the menu endpoint
        client = APIClient()
        response = client.get('/restaurant/menu/')

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Assert that the response data matches the serialized data
        self.assertEqual(response.data, serializer.data)
