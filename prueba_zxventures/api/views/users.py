"""Vista de control de rutas de creación de usuarios."""

from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from ..serializers import UserSerializer

class UserView(APIView):
    """Vista de API de creación de usuarios."""
    def post(self, request):
        """Crea un nuevo usuario en el sistema."""
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)