
from apps.docentes.models import Teacher
from rest_framework import serializers
from django_countries.serializers import CountryFieldMixin

class TeacherSerializer(CountryFieldMixin, serializers.ModelSerializer):
    
    class Meta:
        model= Teacher
        fields = ('__all__')
        #exclude = ('created_date', 'deleted_date', 'delete_motive', 'state')