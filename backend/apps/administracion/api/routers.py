"""rest URL Configuration"""

from django.urls import path,include

from rest_framework.routers import DefaultRouter
from apps.administracion.api.views.general_views import CategoryViewset, PositionViewset
from apps.administracion.api.views.position_views import Position_TeacherViewSet
from apps.administracion.api.api import LevelViewSet

router = DefaultRouter()

router.register(r'administracion/cargo_docente', Position_TeacherViewSet, basename = 'position_teacher')
router.register(r'administracion/categoria', CategoryViewset, basename = 'categoria')
router.register(r'administracion/cargo', PositionViewset, basename = 'cargo')
router.register(r'api/nivel', LevelViewSet)
# router.register(r'api/modalidad', api.SpecialityViewSet)
# router.register(r'api/categoria_cargo', general_views.CategoryListAPIView, 'categoria_cargo')

urlpatterns = router.urls

# urlpatterns = [
#     path(r'api/categoria_cargo', general_views.CategoryListAPIView.as_view(), name='categoria_cargo'),
#     path(r'api/cargo', general_views.PositionListAPIView.as_view(), name='cargo'),
#     path(r'api/cargo_docente', Position_TeacherListCreateAPIView.as_view(), name='cargo_docente_list'),
#     path(r'api/cargo_docente/<int:pk>', Position_TeacherRetrieveUpdateDestroyAPIView.as_view(), name='cargo_docente_retrieveupdatedestroy'),
# ]