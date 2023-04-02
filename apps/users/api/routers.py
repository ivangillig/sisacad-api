from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.users.api.views.general_views import UserViewset, CheckUserViewset, PersonViewset, CustomRegisterView

router = DefaultRouter()

router.register('secretaria/user', UserViewset, basename='user'),
router.register('administracion/person', PersonViewset, basename='person')
router.register('administracion/checkemail', CheckUserViewset, basename='checkemail')

urlpatterns = router.urls



