
from administracion.models import Curso, Nivel
from rest_framework import viewsets, permissions
from administracion.serializers import CursoSerializer, NivelSerializer

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all().order_by('-id')
    serializer_class = CursoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class NivelViewSet(viewsets.ModelViewSet):

    queryset = Nivel.objects.all() 
    serializer_class = NivelSerializer
    # permission_classes = [permissions.IsAuthenticated]