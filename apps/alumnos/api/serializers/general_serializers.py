from rest_framework import serializers
from apps.alumnos.models import Student, Tutor, Student_Tutor, Payment


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
        fields = '__all__'
        