from django.contrib.auth.models import User
from administracion.models import Alumno, Curso, Nivel
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class AlumnoSerializer(serializers.ModelSerializer):
    #dni = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Alumno
        fields = ('dni', 'nombre1', 'nombre2', 'apellido1', 'fecha_ingreso', 'genero')
        read_only_fields = ('fecha_ingreso', )
        #fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
    cursos = AlumnoSerializer(many=True)
    class Meta:
        model = Curso
        fields = ('curso', 'division_curso', 'cursos')

class NivelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nivel
        fields = ('id', 'nombre', 'estado', 'created_at')