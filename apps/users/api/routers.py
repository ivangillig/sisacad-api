from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.users.api.views.general_views import UserViewset, PersonViewset, CheckUserViewset

router = DefaultRouter()

router.register('secretaria/user', UserViewset, basename='user')
router.register('secretaria/person', PersonViewset, basename='person')
router.register('secretaria/checkemail', CheckUserViewset, basename='checkemail')

urlpatterns = [
    path('secretaria/', include(router.urls)),
]



