"""Vistas de control de rutas para manipulación de proveedores."""

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import GeometryDistance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated 

from ..models import Provider
from ..serializers import ProviderSerializer

class ProviderView(APIView):
    """Vista de API de manipulación de proveedores."""
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk=None):
        """"Lee los datos de un proveedor.
        
        Si se indica un identificador (`pk`), se intenta leer los datos del
        proveedor que corresponda. De lo contrario, se espera que se indiquen
        latitud y longitud de una ubicación, para leer los datos del proveedor
        cuya área de cobertura incluya el punto indicado y cuya dirección sea
        la más cercana a la ubicación especificada."""
        try:
            if pk:
                provider = Provider.objects.get(pk=pk)
                serializer = ProviderSerializer(provider)
                return Response(serializer.data)
            elif request.query_params:
                lat = request.GET.get('lat', None)
                lng = request.GET.get('lng', None)
                if lat and lng:
                    location = Point(float(lat), float(lng))
                    providers = Provider.objects.\
                        filter(coverageArea__contains=location).\
                        annotate(distance=GeometryDistance('address', location)).\
                        order_by('distance')
                    if providers:
                        serializer = ProviderSerializer(providers[0])
                        return Response(serializer.data, status=200)
                    else:
                        return Response(status=204)
            return Response({'error': 'Missing parameters ({})'.format(','.join([ x for x in ['lat', 'lng'] if x not in  list(request.query_params.keys())]))}, status=400)
        except Provider.DoesNotExist:
            return Response(status=404)
        except ValueError as e:
            return Response({'error': str(e)}, status=400)
    
    def post(self, request):
        """Crea un nuevo proveedor en el sistema."""
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
