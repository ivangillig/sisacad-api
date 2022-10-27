##VISTAS GENERICAS CON LISTAPIVIEW - REEMPLAZAR POR VIEWSET
from rest_framework import generics

from apps.administracion.models import Level
from apps.administracion.api.serializers.serializers import LevelSerializer

class LevelListAPIView(generics.ListAPIView):
    serializer_class = LevelSerializer

    def get_queryset(self):
        return super().get_queryset()
    