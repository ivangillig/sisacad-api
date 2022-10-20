from django.shortcuts import render
from django.contrib.auth.models import User
from administracion.models import Alumno, Curso

from rest_framework import viewsets
from rest_framework import permissions
from administracion.serializers import AlumnoSerializer, UserSerializer, CursoSerializer


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class AlumnoViewSet(viewsets.ModelViewSet):

    queryset = Alumno.objects.all().order_by('-nombre1')
    serializer_class = AlumnoSerializer
    # permission_classes = [permissions.IsAuthenticated]

class CursoViewSet(viewsets.ModelViewSet):

    queryset = Curso.objects.all().order_by('-id')
    serializer_class = CursoSerializer
    # permission_classes = [permissions.IsAuthenticated]
