from rest_framework import serializers
from rest_framework_gis import serializers as serializers_gis
from .models import Provider

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = [ "id", "tradingName", "ownerName", "document", "coverageArea", "address" ]