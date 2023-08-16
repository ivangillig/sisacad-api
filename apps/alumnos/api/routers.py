from rest_framework import routers
from apps.alumnos.api.views.general_views import PaymentViewSet
from apps.alumnos.api.views.student_views import PaymentAndPaymentStudentViewSet, StudentViewSet, TutorViewSet, Student_TutorViewSet, Withdraw_AuthorizedViewSet, Student_Withdraw_AuthorizedViewSet


router = routers.DefaultRouter()

router.register(r'secretaria/alumno', StudentViewSet, basename='students')
router.register(r'tutores', TutorViewSet, basename='tutors')
router.register(r'alumnostutores', Student_TutorViewSet, basename='student_tutors')
router.register(r'autorizados', Withdraw_AuthorizedViewSet, basename='withdraw_authorizeds')
router.register(r'alumnosautorizados', Student_Withdraw_AuthorizedViewSet, basename='student_withdraw_authorizeds')
router.register(r'pagos', PaymentViewSet, basename='payments')
router.register(r'pagos-completos', PaymentAndPaymentStudentViewSet, basename='payment_and_student')

urlpatterns = router.urls


# apps/students/urls.py

