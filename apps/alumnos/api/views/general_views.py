# apps/alumnos/api/views/general_views.py
from urllib import response
from rest_framework import serializers

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from apps.alumnos.models import Student, Tutor, Student_Tutor, Withdraw_Authorized, Student_Withdraw_Authorized, Payment
from apps.alumnos.api.serializers.general_serializers import StudentSerializer, TutorSerializer, Student_TutorSerializer, Withdraw_AuthorizedSerializer, Student_Withdraw_AuthorizedSerializer, PaymentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    #permission_classes = [IsAuthenticated]

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

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    #permission_classes = [IsAuthenticated]