from django.contrib.auth.models import User
from alumnos.models import Alumno
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'groups']

class AlumnoSerializer(serializers.ModelSerializer):
    #dni = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Alumno
        fields = ('dni', 'nombre1', 'nombre2', 'apellido1')
        read_only_fields = ('fecha_ingreso', )
        #fields = '__all__'