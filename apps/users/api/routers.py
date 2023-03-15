"""rest URL Configuration"""

from django.urls import path,include

from rest_framework.routers import DefaultRouter
from apps.users.api.views.general_views import UserViewset, PersonViewset, CheckUserViewset

router = DefaultRouter()

router.register(r'secretaria/user', UserViewset, basename = 'usuario'),
router.register(r'secretaria/person', PersonViewset, basename = 'persona'),
router.register(r'secretaria/checkemail', CheckUserViewset, basename = 'check_email'),

urlpatterns = router.urls
