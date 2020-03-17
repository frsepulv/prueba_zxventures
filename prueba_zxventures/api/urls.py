"""
Rutas de aplicación 'api'.

La aplicación soporta 3 operaciones:

- POST sobre `providers/```, para crear un nuevo proveedor.
- GET sobre `providers/?lat=N&lng=N`, para encontrar el proveedor más cercano.
- GET sobre `providers/{pk}`, para obtener los datos de un proveedor específico.
"""

from django.urls import path
from .views import ProviderView, UserView

urlpatterns = [
    path('providers/', ProviderView.as_view()),
    path('providers/<int:pk>/', ProviderView.as_view()),
    path('users/', UserView.as_view()),
]