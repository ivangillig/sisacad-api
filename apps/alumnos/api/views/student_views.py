# apps/alumnos/api/views/general_views.py
from urllib import response
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.alumnos.models import Student, Tutor, Student_Tutor, Withdraw_Authorized, Student_Withdraw_Authorized, Payment
from apps.alumnos.api.serializers.general_serializers import TutorSerializer, Student_TutorSerializer, PaymentSerializer
from apps.alumnos.api.serializers.student_serializer import StudentSerializer, Withdraw_AuthorizedSerializer, Student_Withdraw_AuthorizedSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    #permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        students_ids = request.data.get('students_ids', [])
        if not students_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            students = Student.objects.filter(id__in=students_ids)
            students.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar alumnos', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TutorViewSet(viewsets.ModelViewSet):
    serializer_class = TutorSerializer
    queryset = Tutor.objects.all()
    #permission_classes = [IsAuthenticated]

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id = pk).first() 

class Student_TutorViewSet(viewsets.ModelViewSet):
    serializer_class = Student_TutorSerializer
    queryset = Student_Tutor.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return Student_TutorSerializer
        else:
            # Aquí especificas un serializer diferente para la acción retrieve
            # que incluirá la información de los modelos foráneos
            return StudentTutorWithRelatedSerializer

class StudentTutorWithRelatedSerializer(serializers.ModelSerializer):
    student = StudentSerializer()
    tutor = TutorSerializer()

    class Meta:
        model = Student_Tutor
        fields = '__all__'

class Withdraw_AuthorizedViewSet(viewsets.ModelViewSet):
    serializer_class = Withdraw_AuthorizedSerializer
    queryset = Withdraw_Authorized.objects.all()
    #permission_classes = [IsAuthenticated]

class Student_Withdraw_AuthorizedViewSet(viewsets.ModelViewSet):
    serializer_class = Student_Withdraw_AuthorizedSerializer
    queryset = Student_Withdraw_Authorized.objects.all()
    #permission_classes = [IsAuthenticated]