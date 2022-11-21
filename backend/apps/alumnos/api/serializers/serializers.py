from apps.alumnos.models import Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    #dni = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Student
        #fields = ('id', 'doc_number', 'first_name', 'middle_name', 'first_lastname', 'birthday', 'gender')
        exclude = ('state', 'created_date', 'deleted_date',)
        read_only_fields = ('admission_date', )
        