from django.urls import path, include

urlpatterns = [
    path('', include('prueba_zxventures.api.urls')),
]