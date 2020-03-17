"""Serializadores de objetos del modelo de datos."""

from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    """Serializador de proveedores de cerveza."""
    class Meta:
        model = Provider
        fields = [ "id", "tradingName", "ownerName", "document", "coverageArea", "address" ]

class UserSerializer(serializers.Serializer):
    """Serializador simplificado de usuarios para autenticación."""
    username = serializers.CharField(max_length=150, required=True)
    password = serializers.CharField(required=True)
    email = serializers.CharField(required=False)

    def create(self, validated_data):
        """Crea un nuevo usuario en el sistema."""
        return User.objects.create_superuser(**validated_data)