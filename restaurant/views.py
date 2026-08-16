from datetime import datetime

from django.shortcuts import render
from rest_framework import generics, viewsets

# Step 2: Import the IsAuthenticated permission class
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Render the home page and pass the current year to the template


def index(request):
    return render(request, 'index.html', {'current_year': datetime.now().year})

# Handles GET (list all items) and POST (create a new item) for Menu


class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET / PUT / PATCH / DELETE for a single Menu item by its id


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Provides default CRUD operations (GET, POST, PUT, DELETE) for Bookings


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    # Step 3: Secure the booking API - only authenticated users can access it
    permission_classes = [IsAuthenticated]
