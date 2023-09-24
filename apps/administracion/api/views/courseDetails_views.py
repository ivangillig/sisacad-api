from xml.dom import ValidationErr
from django.db import IntegrityError
from apps.alumnos.api.serializers.student_serializer import StudentSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

import json
from django.http import JsonResponse

from apps.alumnos.models import Student
from apps.administracion.models import Course_Student, Level, Division, Speciality, Course, Grade
from apps.administracion.api.serializers.courseDetails_serializers import CourseSerializer, CourseStudentSerializer, LevelSerializer, SpecialitySerializer, DivisionSerializer, GradeSerializer

class LevelViewSet(viewsets.ModelViewSet):

    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        level_name = request.data.get('name')
        if Level.objects.filter(name=level_name).exists():
            return Response({'message': 'Ya existe un nivel con ese nombre.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        level_name = request.data.get('name')
        if Level.objects.filter(name=level_name).exclude(pk=kwargs.get('pk')).exists():
            return Response({'message': 'Ya existe un nivel con ese nombre.'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        level_ids = request.data.get('level_ids', [])
        if not level_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            levels = Level.objects.filter(id__in=level_ids)
            levels.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar niveles', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SpecialityViewSet(viewsets.ModelViewSet):

    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        speciality_ids = request.data.get('speciality_ids', [])
        if not speciality_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            specialities = Speciality.objects.filter(id__in=speciality_ids)
            specialities.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar divisiones', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DivisionViewSet(viewsets.ModelViewSet):

    queryset = Division.objects.all() 
    serializer_class = DivisionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        division_ids = request.data.get('division_ids', [])
        if not division_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            divisions = Division.objects.filter(id__in=division_ids)
            divisions.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar divisiones', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GradeViewSet(viewsets.ModelViewSet):

    queryset = Grade.objects.all() 
    serializer_class = GradeSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        grade_ids = request.data.get('grade_ids', [])
        if not grade_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            grades = Grade.objects.filter(id__in=grade_ids)
            grades.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar años', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['post'])
    def create_grade(self, request):
        # Parse JSON data from the request body
        data = json.loads(request.body)

        # Get the level instance with the specified ID
        level = Level.objects.get(id=data['level'])

        # Get the speciality instance, or null if data doesn't contain a value for speciality
        division = Division.objects.get(id=data.get('division')) if data.get('division') else None
        speciality = Speciality.objects.get(id=data.get('speciality')) if data.get('speciality') else None


        # Create the new Grade instance
        grade = Grade.objects.create(
            level=level,
            name=data['name'],
            speciality=speciality,
            division=division
        )

        # Serialize the new grade instance and return as JSON
        serializer = self.serializer_class(grade)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk=None):
        # Get the instance of Grade being updated
        grade = self.get_object()

        # Parse JSON data from the request body
        data = json.loads(request.body)

        # Print the request data for debugging purposes
        print(request.data)

        # Update the instance of Grade with the new data
        grade.name = data.get('name', grade.name)
        grade.speciality = Speciality.objects.get(id=data.get('speciality')) if data.get('speciality') else None
        grade.division = Division.objects.get(id=data.get('division')) if data.get('division') else None
        grade.level = Level.objects.get(id=data.get('level', grade.level.id))
        grade.save()

        # Serialize the updated grade instance and return as JSON
        serializer = self.serializer_class(grade)
        return Response(serializer.data)

class CourseViewSet(viewsets.ModelViewSet):
    #queryset = Course.objects.all()
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Opcionalmente restringe el conjunto de consultas devuelto por año académico,
        al filtrar contra un parámetro `academic_year` en la URL.
        """
        queryset = Course.objects.all()
        academic_year = self.request.query_params.get('academic_year', None)
        if academic_year:
            try:
                # Convert the format "YYYY-01-01" to "YYYY" in order to filter
                year_only = academic_year.split('-')[0]
                queryset = queryset.filter(academic_year=year_only)
            except IndexError:
                raise ValidationErr({"error": "Formato de año académico inválido."})
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data

        grade = Grade.objects.get(id=data.get('grade')) if data.get('grade') else None
        academic_year = data['academic_year']
        shift = data['shift']

        try:
            Course.objects.create(
                grade=grade,
                academic_year=academic_year,
                shift=shift,
            )
            return Response({'message': 'Curso lectivo creado correctamente'}, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'Ya existe un curso con las mismas especificaciones.'}, status=status.HTTP_400_BAD_REQUEST)

class CourseStudentViewSet(viewsets.ModelViewSet):
    serializer_class = CourseStudentSerializer
    queryset = Course_Student.objects.all()

    @action(detail=False, methods=['get'], url_path='curso/(?P<course_id>\d+)')
    def students_in_course(self, request, course_id=None):
        """
        Retrieve students in a specific course.

        This endpoint returns a list of students who are enrolled in the specified course.

        Parameters:
        - course_id: The ID of the course for which to retrieve the students.

        Returns:
        - 200 OK: A list of students in the specified course.
        """
        students = Course_Student.objects.filter(course__id=course_id)
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='current_course/(?P<student_id>\\d+)')
    def current_course_for_student(self, request, student_id=None):
        """
        Retrieve the current active course for a specific student.

        This endpoint returns the active course in which a student is enrolled for the current academic year.

        Parameters:
        - student_id: The ID of the student for whom to retrieve the current course.

        Returns:
        - 200 OK: The active course for the student for the current academic year.
        - 404 Not Found: If no active course is found for the student for the current academic year.
        """
        from datetime import date
        current_year = date.today().year
        course_student = Course_Student.objects.filter(student__id=student_id, course__academic_year=current_year, state=True).first()
        if course_student:
            serializer = self.get_serializer(course_student)
            return Response(serializer.data)
        return Response({'message': 'No se encontró un curso actual para el estudiante'}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request, *args, **kwargs):
        """
        Enroll a student in a course.

        This endpoint allows you to enroll a student in a specific course.
        It checks if the student is already enrolled in an active course for the same academic year
        and returns an error if that's the case.

        Parameters:
        - course: The ID of the course in which the student will be enrolled.
        - student: The ID of the student to be enrolled.
        - add_date: The date on which the student is added to the course.

        Returns:
        - 201 Created: If the student is successfully enrolled.
        - 400 Bad Request: If the student is already enrolled in an active course for the same academic year.
        - 500 Internal Server Error: For other unexpected errors.
        """
        data = request.data

        try:
            course = Course.objects.get(id=data.get('course')) if data.get('course') else None
            student = Student.objects.get(id=data.get('student')) if data.get('student') else None
            add_date = data['add_date']

            # Check if the student is already enrolled in an active course for the same academic year
            existing_course_student = Course_Student.objects.filter(
                student=student,
                course__academic_year=course.academic_year,
                state=True
            ).first()

            if existing_course_student:
                return Response({'message': 'El estudiante ya está matriculado en un curso activo para este año'}, status=status.HTTP_400_BAD_REQUEST)

            Course_Student.objects.create(
                course=course,
                student=student,
                add_date=add_date
            )

            return Response({'message': 'Alumno matriculado correctamente'}, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response({'message': 'Parece que este alumno ya está matriculado'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({'message': f'Error inesperado: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

