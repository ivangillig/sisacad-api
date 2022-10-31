##VISTAS GENERICAS CON LISTAPIVIEW - REEMPLAZAR POR VIEWSET
from rest_framework import generics

from apps.base.api import GeneralListApiView
from apps.administracion.api.serializers.general_serializers import LevelSerializer, CategorySerializer, PositionSerializer

# class LevelListAPIView(generics.ListAPIView):
#     serializer_class = LevelSerializer

#     def get_queryset(self):
#         return super().get_queryset()
    

class CategoryListAPIView(GeneralListApiView):
    serializer_class = CategorySerializer

class PositionListAPIView(GeneralListApiView):
    serializer_class = PositionSerializer