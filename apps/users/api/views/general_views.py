from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from apps.users.models import Person
from django.shortcuts import get_object_or_404

import json
from apps.users.api.serializers.general_serializers import UserSerializer, PersonSerializer

class UserViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True) 
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active = True).first() 

class CheckUserViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def create(self, request):

        data = json.loads(request.body)
        print(data['email'])
        
        email = self.get_serializer().Meta.model.objects.filter(email = data['email'])

        if not email:
            return Response({'message': 'No existe ningún alumno con este email'}, status = status.HTTP_200_OK)
        return Response({'message': 'Esta cuenta institucional ya se encuentra en uso!'}, status=status.HTTP_400_BAD_REQUEST)

class PersonViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    
    serializer_class = PersonSerializer
    queryset = PersonSerializer.Meta.model.objects.all()
    lookup_field = 'doc_number'

        
    # def get_obect(self, dni):
    #     return get_object_or_404 (self.model.Meta.model, doc_number = dni)
 
    

# class PositionViewset(viewsets.ModelViewSet):
#     #permission_classes = [IsAuthenticated]

#     serializer_class = PositionSerializer

#     def get_queryset(self, pk = None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.filter(state = True) 
#         return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first() 