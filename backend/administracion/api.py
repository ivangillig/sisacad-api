
from administracion.models import Alumno, Curso
from rest_framework import viewsets, permissions
from administracion.serializers import AlumnoSerializer, CursoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):

    queryset = Alumno.objects.all() #.order_by('-nombre1')
    serializer_class = AlumnoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all().order_by('-id')
    serializer_class = CursoSerializer
    # permission_classes = [permissions.IsAuthenticated]