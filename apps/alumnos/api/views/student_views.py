# apps/alumnos/api/views/general_views.py
from urllib import response
from django.conf import settings

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from apps.alumnos.models import Payment_Student, Student, Tutor, Student_Tutor, Withdraw_Authorized, Student_Withdraw_Authorized
from apps.alumnos.api.serializers.general_serializers import TutorSerializer, Student_TutorSerializer, PaymentStudentSerializer, PaymentSerializer
from apps.alumnos.api.serializers.student_serializer import StudentSerializer, Withdraw_AuthorizedSerializer, Student_Withdraw_AuthorizedSerializer

website_url = settings.MY_WEBSITE_URL

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    #permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        if response.status_code == 201:
            student = Student.objects.get(id=response.data['id'])

            context = {
                'student_name': student.first_name,
                'student_email': student.user.email,
                'website_url': website_url,
                'student': student
            }
            email_body = render_to_string('newStudent.html', context)

            email = EmailMessage(
                'Bienvenido/a a nuestra institución',
                email_body,
                'juvenilinstitutofueguino@jif.com.ar',
                [student.user.email]
            )
            email.content_subtype = 'html'
            email.send()

        return response

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

class PaymentAndPaymentStudentViewSet(viewsets.GenericViewSet):
    queryset = Payment_Student.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return PaymentSerializer
        return PaymentStudentSerializer

    def create(self, request, *args, **kwargs):
        payment_serializer = self.get_serializer_class()(data=request.data)

        if payment_serializer.is_valid():
            payment = payment_serializer.save()

            # Obtener el correo electrónico y el nombre del estudiante
            student = Student.objects.get(id=request.data['student_id'])

            # Obtener el correo electrónico del User asociado al Student a través de Person
            student_email = student.user.email

            # Renderizar la plantilla con el contexto
            context = {
                'student_name': student.first_name,
                'payment_date': request.data['payment_date'],
                'amount': request.data['amount'],
                'website_url': website_url
            }
            email_body = render_to_string('payment_received.html', context)

            # Enviar el correo
            email = EmailMessage(
                'Nuevo comprobante de pago recibido',
                email_body,
                'juvenilinstitutofueguino@jif.com.ar',
                [student_email]
            )
            email.content_subtype = 'html'  # Para enviar el correo en formato HTML
            email.send()

            payment_student_data = {
                'student': request.data['student_id'],
                'payment': payment.id
            }
            print(payment_student_data)

            payment_student_serializer = PaymentStudentSerializer(data=payment_student_data)
            if payment_student_serializer.is_valid():
                payment_student_serializer.save()
                return Response({'message': 'Pago cargado correctamente'}, status=status.HTTP_201_CREATED)

            payment.delete()
            return Response(payment_student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        Payment_Student = self.get_object()
        serializer = self.get_serializer_class()(Payment_Student)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def payments_by_student(self, request):
        student_id = request.query_params.get('student_id', None)
        if not student_id:
            return Response({'message': 'Se requiere un ID de estudiante'}, status=status.HTTP_400_BAD_REQUEST)

        payments_by_student = Payment_Student.objects.filter(student__id=student_id)
        serializer = self.get_serializer_class()(payments_by_student, many=True)
        return Response(serializer.data)
