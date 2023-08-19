from apps.alumnos.api.serializers.student_serializer import StudentSerializer
from rest_framework import serializers
from apps.alumnos.models import Payment_Student, Student, Tutor, Student_Tutor, Payment


class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class Student_TutorSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    tutor = serializers.PrimaryKeyRelatedField(queryset=Tutor.objects.all())
    relationship = serializers.CharField()

    class Meta:
        model = Student_Tutor
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'amount', 'payment_date', 'file', 'payment_type')

class PaymentStudentSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    payment = serializers.PrimaryKeyRelatedField(queryset=Payment.objects.all())

    student_details = StudentSerializer(source='student', read_only=True)
    payment_details = PaymentSerializer(source='payment', read_only=True)

    class Meta:
        model = Payment_Student
        fields = '__all__'

