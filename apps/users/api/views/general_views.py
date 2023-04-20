from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from dj_rest_auth.registration.views import RegisterView

from apps.users.models import Person
from django.shortcuts import get_object_or_404

import json
from apps.users.api.serializers.general_serializers import UserSerializer, PersonSerializer, CustomRegisterSerializer

class UserViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True) 
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active = True).first() 

#dj-rest-auth modified for retrieve the id and mail
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(request)
        data = {
            'id': user.id,
            'email': user.email,
        }
        return Response(data, status=status.HTTP_201_CREATED)

class CheckUserViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def create(self, request):

        data = json.loads(request.body)        
        email = self.get_serializer().Meta.model.objects.filter(email = data['email'])

        if not email:
            return Response({'success': False, 'message': 'No se encontró ninguna cuenta de correo asociada al mail proporcionado.'}, status = status.HTTP_200_OK)
        return Response({'success': True, 'message': 'Esta cuenta institucional ya se encuentra en uso'}, status=status.HTTP_400_BAD_REQUEST)

class PersonViewset(viewsets.ViewSet):
    serializer_class = PersonSerializer
    queryset = PersonSerializer.Meta.model.objects.all() # Definimos el queryset

    
    def retrieve(self, request, pk=None):
        try:
            person = Person.objects.get(doc_number=pk)
            serializer = self.serializer_class(person)
            return Response({'success': True, 'data' : serializer.data })
        except Person.DoesNotExist:
            return Response({'success': False, 'message': 'No se encontró la persona con el DNI proporcionado.'}, status=200)


# class PositionViewset(viewsets.ModelViewSet):
#     #permission_classes = [IsAuthenticated]

#     serializer_class = PositionSerializer

#     def get_queryset(self, pk = None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.filter(state = True) 
#         return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first() 