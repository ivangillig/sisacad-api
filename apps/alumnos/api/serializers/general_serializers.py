from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from apps.alumnos.models import Student, Tutor, Student_Tutor, Withdraw_Authorized, Student_Withdraw_Authorized, Payment


class StudentSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


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


class Withdraw_AuthorizedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw_Authorized
        fields = '__all__'


class Student_Withdraw_AuthorizedSerializer(serializers.ModelSerializer):
    withdraw_authorized = Withdraw_AuthorizedSerializer()
    student = StudentSerializer()

    class Meta:
        model = Student_Withdraw_Authorized
        fields = '__all__'
        depth = 1


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        