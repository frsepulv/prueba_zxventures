from rest_framework import serializers
from rest_framework_gis import serializers as serializers_gis
from .api.models import Provider

class ProviderSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    tradingName = serializers.CharField(max_length=64)
    ownerName = serializers.CharField(max_length=64)
    document = serializers.CharField(max_length=32, unique=True)
    coverageArea = serializers_gis.MultiPolygonField()
    address = serializers_gis.PointField()

    def create(self, validated_data):
        return Provider.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.tradingName = validated_data.get('tradingName', instance.tradingName)
        instance.ownerName = validated_data.get('ownerName', instance.ownerName)
        instance.document = validated_data.get('document', instance.document)
        instance.coverageArea = validated_data.get('coverageArea', instance.coverageArea)
        instance.address = validated_data.get('address', instance.address)