# App-level URL configuration
from django.urls import path
from . import views

# Import obtain_auth_token view to issue tokens via API
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Home page (template uses {% url 'home' %})
    path('', views.index, name='home'),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

    # Menu API: GET list all items | POST create a new item
    path('menu/', views.MenuItemView.as_view(), name='menu-list'),

    # Menu API: GET / PUT / DELETE a single item by id
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
]
