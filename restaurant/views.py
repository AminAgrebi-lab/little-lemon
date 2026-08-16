from datetime import datetime

from django.shortcuts import render
from rest_framework import generics

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Render the home page and pass the current year to the template


def index(request):
    return render(request, 'index.html', {'current_year': datetime.now().year})

# Handles GET (list all items) and POST (create a new item)


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET / PUT / PATCH / DELETE for a single item by its id


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (list all bookings) and POST (create a new booking)


class BookingView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
