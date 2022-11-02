##VISTAS GENERICAS CON LISTAPIVIEW - REEMPLAZAR POR VIEWSET
from rest_framework import generics, status
from rest_framework.response import Response

from apps.base.api import GeneralListApiView
from apps.administracion.api.serializers.position_serializers import Position_TeacherSerializer
    
class Position_TeacherListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = Position_TeacherSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True) 

    def post (self, request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cargo asociado correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#Alternativa al get
class Position_TeacherRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = Position_TeacherSerializer
    
    def get_queryset(self, pk = None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True) 
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first() 
            

    def patch(self,request,pk=None):
        if self.get_queryset(pk):
            position_teacher_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(position_teacher_serializer.data, status =  status.HTTP_200_OK)
        return Response({'error': 'No existe un cargo con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk = None):
        if self.get_queryset(pk):
            position_teacher_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if position_teacher_serializer.is_valid():
                position_teacher_serializer.save()
                return Response(position_teacher_serializer.data, status =  status.HTTP_200_OK)
            return Response(position_teacher_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        position_teacher = self.get_queryset().filter(id = pk).first()
        if position_teacher:
            position_teacher.state = False
            position_teacher.save()
            return Response({'message': 'Producto eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un cargo con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)


