"""rest URL Configuration"""

from rest_framework.routers import DefaultRouter
from apps.administracion.api.views.general_views import CategoryViewset, PositionViewset, BankViewSet
from apps.administracion.api.views.courseDetails_views import CourseStudentViewSet, CourseViewSet, LevelViewSet, DivisionViewSet, SpecialityViewSet, GradeViewSet
from apps.administracion.api.views.position_views import Position_TeacherViewSet

router = DefaultRouter()

router.register(r'secretaria/cargo_docente', Position_TeacherViewSet, basename = 'position_teacher')
router.register(r'secretaria/categoria', CategoryViewset, basename = 'categoria')
router.register(r'secretaria/cargo', PositionViewset, basename = 'cargo')
router.register(r'secretaria/banks', BankViewSet, basename='bank')
router.register(r'secretaria/nivel', LevelViewSet)
router.register(r'secretaria/division', DivisionViewSet, basename='division')
router.register(r'secretaria/modalidad', SpecialityViewSet, basename='modalidad')
router.register(r'secretaria/grado', GradeViewSet, basename='grado')
router.register(r'secretaria/curso', CourseViewSet, basename='curso')
router.register(r'secretaria/curso_alumno', CourseStudentViewSet, basename='curso_alumno')


# router.register(r'secretaria/division/delete_multiple', DivisionViewSet.as_view({'post': 'delete_multiple'}), basename='delete_multiple')

# router.register(r'api/modalidad', api.SpecialityViewSet)
# router.register(r'api/categoria_cargo', general_views.CategoryListAPIView, 'categoria_cargo')

urlpatterns = router.urls
