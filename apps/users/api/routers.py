from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.users.api.views.general_views import UserViewset, CheckUserViewset, PersonViewset

router = DefaultRouter()

router.register('administracion/user', UserViewset, basename='user')
router.register('administracion/person', PersonViewset, basename='person')
router.register('administracion/checkemail', CheckUserViewset, basename='checkemail')

urlpatterns = [
    path('secretaria/', include(router.urls)),
]



