from rest_framework import routers
from alumnos import api
from alumnos import views


router = routers.DefaultRouter()

router.register('api/alumno', api.AlumnoViewSet)

urlpatterns = router.urls