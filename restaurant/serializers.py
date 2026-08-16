# Import ModelSerializer and the app models
from rest_framework import serializers
from .models import Menu, Booking

# Converts Menu model instances to JSON and validates incoming data


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']

# Converts Booking model instances to JSON and validates incoming data


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        # Include all fields from the Booking model (as required by the exercise)
        fields = '__all__'
