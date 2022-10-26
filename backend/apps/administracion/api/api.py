
from apps.administracion.models import Course, Level, Speciality
from rest_framework import viewsets, permissions
from apps.administracion.api.serializers.serializers import CourseSerializer, LevelSerializer, SpecialitySerializer


class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

class LevelViewSet(viewsets.ModelViewSet):

    queryset = Level.objects.all() 
    serializer_class = LevelSerializer
    # permission_classes = [permissions.IsAuthenticated]

class SpecialityViewSet(viewsets.ModelViewSet):

    queryset = Speciality.objects.all() 
    serializer_class = SpecialitySerializer
    # permission_classes = [permissions.IsAuthenticated]