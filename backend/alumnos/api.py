
from alumnos.models import Alumno
from rest_framework import viewsets, permissions
from alumnos.serializers import AlumnoSerializer

class AlumnoViewSet(viewsets.ModelViewSet):

    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    # permission_classes = [permissions.IsAuthenticated]
