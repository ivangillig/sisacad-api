from apps.users.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    #cursos = AlumnoSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'email')


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')