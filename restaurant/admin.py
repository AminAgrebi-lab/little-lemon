# Import Django admin module
from django.contrib import admin

# Import the Menu and Booking models from the restaurant app
from .models import Menu, Booking

# Register models to manage them via the Django admin interface
admin.site.register(Menu)
admin.site.register(Booking)
