from apps.administracion.models import Course, Level, Speciality, Position, Category
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
        fields = ('id', 'name', 'state', 'created_date') #, 'created_by'

class SpecialitySerializer(serializers.ModelSerializer):
    #created_by = AlumnoSerializer(source='docente')

    class Meta:
        model = Speciality
        fields = ('id', 'name', 'state') #, 'created_by'
        #exclude = ('state',)

class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_date', 'deleted_date', 'state',)

class PositionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Position
        exclude = ('created_date', 'deleted_date', 'place_number2')