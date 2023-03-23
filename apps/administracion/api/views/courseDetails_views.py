##VISTAS GENERICAS CON LISTAPIVIEW - REEMPLAZAR POR VIEWSET
from apps.administracion.models import Level, Division, Speciality, Course
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action


from apps.administracion.api.serializers.courseDetails_serializers import CourseSerializer, LevelSerializer, SpecialitySerializer, DivisionSerializer

class CourseViewSet(viewsets.ModelViewSet):

    queryset = Course.objects.all().order_by('-id')
    serializer_class = CourseSerializer
    # permission_classes = [permissions.IsAuthenticated]

class LevelViewSet(viewsets.ModelViewSet):

    queryset = Level.objects.all() 
    serializer_class = LevelSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        level_ids = request.data.get('level_ids', [])
        if not level_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            levels = Level.objects.filter(id__in=level_ids)
            levels.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar niveles', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SpecialityViewSet(viewsets.ModelViewSet):

    queryset = Speciality.objects.all() 
    serializer_class = SpecialitySerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        speciality_ids = request.data.get('speciality_ids', [])
        if not speciality_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            specialities = Speciality.objects.filter(id__in=speciality_ids)
            specialities.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar divisiones', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DivisionViewSet(viewsets.ModelViewSet):

    queryset = Division.objects.all() 
    serializer_class = DivisionSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'])
    def delete_multiple(self, request):
        division_ids = request.data.get('division_ids', [])
        if not division_ids:
            return Response('Debe proporcionar una lista de ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
        try:
            divisions = Division.objects.filter(id__in=division_ids)
            divisions.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('Error al eliminar divisiones', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

  # @action(detail=False, methods=['post'])
    # def delete_multiple(self, request):
    #     division_ids = request.data.get('division_ids', [])
    #     if not division_ids:
    #         return Response('Debe proporcionar una lista de division_ids para eliminar', status=status.HTTP_400_BAD_REQUEST)
    #     try:
    #         divisions = Division.objects.filter(id__in=division_ids)
    #         divisions.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     except:
    #         return Response('Error al eliminar divisiones', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
