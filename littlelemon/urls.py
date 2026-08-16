# Project-level URL configuration
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restaurant import views

# Register the BookingViewSet under the 'tables' prefix
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurant/', include('restaurant.urls')),
    path('restaurant/booking/', include(router.urls)),

    # Djoser endpoints: registration, users, token login/logout
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
