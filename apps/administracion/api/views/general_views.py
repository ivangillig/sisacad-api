##VISTAS GENERICAS CON LISTAPIVIEW - REEMPLAZAR POR VIEWSET
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.administracion.models import Bank
from apps.administracion.api.serializers.general_serializers import CategorySerializer, PositionSerializer, BankSerializer

class CategoryViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True) 
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first() 

class PositionViewset(viewsets.ModelViewSet):
    #permission_classes = [IsAuthenticated]

    serializer_class = PositionSerializer

    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True) 
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first() 

class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer