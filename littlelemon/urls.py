"""
URL configuration for littlelemon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Project-level URL configuration
from django.contrib import admin
from django.urls import path, include

# Import DefaultRouter and the restaurant views to wire up the ViewSet
from rest_framework.routers import DefaultRouter
from restaurant import views

# Create a router and register the BookingViewSet under the 'tables' prefix
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include restaurant app URLs (Menu API and home page)
    path('restaurant/', include('restaurant.urls')),

    # Include the router URLs for the Booking API
    path('restaurant/booking/', include(router.urls)),
]
