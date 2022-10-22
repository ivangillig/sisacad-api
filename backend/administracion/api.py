
from administracion.models import Alumno, Curso, Nivel
from rest_framework import viewsets, permissions
from administracion.serializers import AlumnoSerializer, CursoSerializer, NivelSerializer

class AlumnoViewSet(viewsets.ModelViewSet):

    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all().order_by('-id')
    serializer_class = CursoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class NivelViewSet(viewsets.ModelViewSet):

    queryset = Nivel.objects.all() 
    serializer_class = NivelSerializer
    # permission_classes = [permissions.IsAuthenticated]