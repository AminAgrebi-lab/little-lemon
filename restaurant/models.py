# Import Django models module
from django.db import models

# Define the Menu model for storing restaurant menu items


class Menu(models.Model):
    # Menu item name with indexing for faster searches
    title = models.CharField(max_length=255, db_index=True)

    # Price with decimal precision (up to 99999.99)
    price = models.DecimalField(max_digits=7, decimal_places=2)

    # Inventory count for stock management
    inventory = models.SmallIntegerField()

    # String representation matching the unit test expectation
    def __str__(self):
        return f'{self.title} : {str(self.price)}'

# Define the Booking model for table reservations


class Booking(models.Model):
    # Customer name
    name = models.CharField(max_length=255)

    # Number of guests (must be positive)
    no_of_guests = models.SmallIntegerField()

    # Reservation date and time
    booking_date = models.DateTimeField()

    # String representation for admin and debugging
    def __str__(self):
        return f'{self.name} - {self.booking_date}'
