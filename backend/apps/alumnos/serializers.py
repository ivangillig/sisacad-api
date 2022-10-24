from django.contrib.auth.models import User
from apps.alumnos.models import Student
from rest_framework import serializers


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'groups']

class StudentSerializer(serializers.ModelSerializer):
    #dni = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Student
        fields = ('doc_number', 'firstname', 'middlename', 'first_lastname')
        read_only_fields = ('admission_date', )
        #fields = '__all__'