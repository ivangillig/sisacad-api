from rest_framework import viewsets
from apps.alumnos.models import Payment
from apps.alumnos.api.serializers.general_serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    #permission_classes = [IsAuthenticated]