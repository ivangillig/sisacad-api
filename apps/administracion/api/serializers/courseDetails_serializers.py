from apps.administracion.models import Course, Level, Division, Speciality, Grade
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

# class GradeSerializer(serializers.ModelSerializer):
#     #created_by = AlumnoSerializer(source='docente')

#     class Meta:
#         model = Grade
#         fields = ('id', 'name', 'division_id', 'level_id', 'speciality_id', 'state', 'created_date')
#         #exclude = ('state',)

class GradeSerializer(serializers.ModelSerializer):
    division = serializers.StringRelatedField()
    level = serializers.StringRelatedField()
    speciality = serializers.StringRelatedField()

    class Meta:
        model = Grade
        fields = ('id', 'name', 'division', 'level', 'speciality', 'state', 'created_date')
