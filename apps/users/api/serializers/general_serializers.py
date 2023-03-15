from apps.users.models import User, Person
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django_countries.serializers import CountryFieldMixin

class UserSerializer(serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'email')

class PersonSerializer(CountryFieldMixin, serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = Person
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')