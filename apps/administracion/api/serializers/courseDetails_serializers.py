from apps.administracion.models import Course, Course_Student, Level, Division, Speciality, Grade
from rest_framework import serializers
from apps.alumnos.api.serializers.student_serializer import StudentSerializer

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

class GradeSerializer(serializers.ModelSerializer):
    division = serializers.StringRelatedField()
    level = serializers.StringRelatedField()
    speciality = serializers.StringRelatedField()

    class Meta:
        model = Grade
        fields = ('id', 'name', 'division', 'level', 'speciality', 'state', 'created_date')


class CourseSerializer(serializers.ModelSerializer):
    grade = GradeSerializer(read_only=True)

    class Meta:
        model = Course
        fields = ('id', 'grade', 'academic_year', 'shift')

class CourseStudentSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    student = StudentSerializer(read_only=True)

    class Meta:
        model = Course_Student
        fields = ['course', 'student', 'add_date', 'leaving_date', 'leaving_motive']