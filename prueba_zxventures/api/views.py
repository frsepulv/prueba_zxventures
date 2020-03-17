from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import Point
from rest_framework.parsers import JSONParser
from .models import Provider
from .serializers import ProviderSerializer

@csrf_exempt
def provider_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProviderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'GET':
        lat = request.GET.get('lat', None)
        lng = request.GET.get('lng', None)
        if lat and lng:
            provider = Provider.objects.filter(coverageArea__contains=Point(float(lat), float(lng)))
            if provider:
                serializer = ProviderSerializer(provider)
                return JsonResponse(serializer.data, status=200)
            else:
                return JsonResponse({}, status=204)
        else:
            return JsonResponse({'error': 'Missing parameters ({}{})'.format("'lat'" if not lat else '', ("'lng'" if lat else ", 'lng'") if not lng else '')}, status=400)
    return JsonResponse({'error': 'Unsupported method: {}'.format(request.method)}, status=405)

@csrf_exempt
def provider_detail(request, pk):
    if request.method == 'GET':
        try:
            provider = Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            return HttpResponse(status=404)
        serializer = ProviderSerializer(provider)
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=405)