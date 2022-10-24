from django.contrib.auth.models import User
from administracion.models import Curso, Nivel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'groups']


class CursoSerializer(serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = Curso
        fields = ('curso', 'division_curso', 'cursos')

class NivelSerializer(serializers.ModelSerializer):
    #created_by = AlumnoSerializer(source='docente')

    class Meta:
        model = Nivel
        fields = ('id', 'nombre', 'estado', 'created_at') #, 'created_by'