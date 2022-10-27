from apps.administracion.models import Course, Level, Speciality
from apps.users.models import  Role
from rest_framework import serializers


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model: Role
        fields = ('__all__')


class CourseSerializer(serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = Course
        fields = ('course', 'division_course', 'courses')

class LevelSerializer(serializers.ModelSerializer):
    #created_by = AlumnoSerializer(source='docente')

    class Meta:
        model = Level
        fields = ('id', 'name', 'state', 'created_date') #, 'created_by'

class SpecialitySerializer(serializers.ModelSerializer):
    #created_by = AlumnoSerializer(source='docente')

    class Meta:
        model = Speciality
        fields = ('id', 'name', 'state') #, 'created_by'
        #exclude = ('state',)