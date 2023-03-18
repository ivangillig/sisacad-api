
from apps.alumnos.models import Student
from rest_framework import viewsets, permissions
from apps.alumnos.api.serializers.general_serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # permission_classes = [permissions.IsAuthenticated]
