"""Rutas del proyecto."""

from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', include('prueba_zxventures.api.urls')),
    path('auth/', obtain_auth_token, name='api_token_auth')
]