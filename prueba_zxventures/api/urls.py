from django.urls import path
from .views import provider_create, provider_detail

urlpatterns = [
    path('providers/', provider_create),
    path('providers/<int:pk>/', provider_detail),
]