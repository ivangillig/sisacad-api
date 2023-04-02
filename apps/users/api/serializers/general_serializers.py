from apps.users.models import User, Person
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django_countries.serializers import CountryFieldMixin
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'email')

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError("Las contraseñas no coinciden.")
        return attrs

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
        }

    def save(self, request):
        user = User.objects.create_user(
            email=self.validated_data['email'],
            password=self.validated_data['password1']
        )
        return user

class PersonSerializer(CountryFieldMixin, serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = Person
        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')