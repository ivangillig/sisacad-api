from apps.administracion.models import Course, Level, Division, Speciality
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = Course
        fields = ('course', 'division_course', 'courses')

class LevelSerializer(serializers.ModelSerializer):
    #created_by = AlumnoSerializer(source='docente')

    class Meta:
        model = Level
        fields = ('id', 'name', 'state', 'created_date')

class DivisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Division
        fields = ('id', 'name', 'state', 'created_date') 

class SpecialitySerializer(serializers.ModelSerializer):
    #created_by = AlumnoSerializer(source='docente')

    class Meta:
        model = Speciality
        fields = ('id', 'name', 'state', 'created_date')
        #exclude = ('state',)
