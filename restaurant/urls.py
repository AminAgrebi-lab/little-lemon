# App-level URL configuration
from django.urls import path
from . import views

urlpatterns = [
    # Home page (template uses {% url 'home' %})
    path('', views.index, name='home'),

    # Menu API: GET list all items | POST create a new item
    path('menu/', views.MenuItemView.as_view(), name='menu-list'),

    # Menu API: GET / PUT / DELETE a single item by id
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),

    # Booking API: GET list all bookings | POST create a new booking
    path('bookings/', views.BookingView.as_view(), name='booking-list'),
]
