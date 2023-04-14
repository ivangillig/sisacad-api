from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin
from apps.alumnos.models import Student, Withdraw_Authorized, Student_Withdraw_Authorized

class StudentSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Student
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