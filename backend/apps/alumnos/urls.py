from rest_framework import routers
from apps.alumnos import api,views


router = routers.DefaultRouter()

router.register('api/alumno', api.StudentViewSet)

urlpatterns = router.urls