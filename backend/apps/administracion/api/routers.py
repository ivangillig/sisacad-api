"""rest URL Configuration"""

from django.urls import path,include

from rest_framework import routers
from apps.administracion.api import api
from apps.administracion import views
from apps.administracion.api.views import general_views
from apps.administracion.api.views.position_views import Position_TeacherListCreateAPIView, Position_TeacherRetrieveUpdateDestroyAPIView

# router = routers.DefaultRouter()

# router.register(r'api/curso', api.CourseViewSet)
# router.register(r'api/nivel', api.LevelViewSet)
# router.register(r'api/modalidad', api.SpecialityViewSet)
# router.register(r'api/categoria_cargo', general_views.CategoryListAPIView, 'categoria_cargo')

# urlpatterns = router.urls

urlpatterns = [
    path(r'api/categoria_cargo', general_views.CategoryListAPIView.as_view(), name='categoria_cargo'),
    path(r'api/cargo', general_views.PositionListAPIView.as_view(), name='cargo'),
    path(r'api/cargo_docente', Position_TeacherListCreateAPIView.as_view(), name='cargo_docente_list'),
    path(r'api/cargo_docente/<int:pk>', Position_TeacherRetrieveUpdateDestroyAPIView.as_view(), name='cargo_docente_retrieveupdatedestroy'),
]