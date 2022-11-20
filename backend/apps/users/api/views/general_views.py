##VISTAS GENERICAS CON LISTAPIVIEW - REEMPLAZAR POR VIEWSET
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.users.api.serializers.general_serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active = True) 
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active = True).first() 

# class PositionViewset(viewsets.ModelViewSet):
#     #permission_classes = [IsAuthenticated]

#     serializer_class = PositionSerializer

#     def get_queryset(self, pk = None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.filter(state = True) 
#         return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first() 