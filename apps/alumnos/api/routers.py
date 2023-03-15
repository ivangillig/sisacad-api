from apps.alumnos.api.api import StudentViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'secretaria/alumno', StudentViewSet)

urlpatterns = router.urls