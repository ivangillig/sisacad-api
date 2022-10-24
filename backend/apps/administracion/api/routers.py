"""rest URL Configuration"""

from rest_framework import routers
from apps.administracion.api import api
from apps.administracion import views

router = routers.DefaultRouter()

router.register(r'api/curso', api.CourseViewSet)
router.register(r'api/nivel', api.LevelViewSet)
router.register(r'api/modalidad', api.SpecialityViewSet)

urlpatterns = router.urls
