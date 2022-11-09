from apps.alumnos.api import api
from rest_framework import routers


router = routers.DefaultRouter()

router.register(r'alumno', api.StudentViewSet)

urlpatterns = router.urls