from django.shortcuts import render
#from django.contrib.auth.models import User

from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework import viewsets, permissions
#from administracion.api.serializers import UserSerializer


# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]

