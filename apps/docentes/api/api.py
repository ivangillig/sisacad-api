from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.docentes.api.serializers.serializer import *
from apps.docentes.models import *

from apps.docentes.models import Bank_Account

class BankAccountViewSet(viewsets.ModelViewSet):
    queryset = Bank_Account.objects.all()
    serializer_class = BankAccountSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'pk'


@api_view(['GET', 'PUT', 'DELETE'])
def bank_account_detail_view(request, pk):

    # queryset
    bank_account = Bank_Account.objects.filter(id = pk).first()
    
    # validation
    if bank_account:
        
        #retrieve
        if request.method == 'GET':
            bank_account_serializer = Bank_AccountSerializer(bank_account)
            return Response(bank_account_serializer.data, status = status.HTTP_200_OK)

        #update
        elif request.method == 'PUT':
            bank_account_serializer = Bank_AccountSerializer(bank_account, data = request.data)
            if bank_account_serializer.is_valid():
                bank_account_serializer.save()
                return Response(bank_account_serializer.data, status = status.HTTP_200_OK)
            return Response(bank_account_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
        #delete
        elif request.method =='DELETE':
            bank_account = Bank_Account.objects.filter(id = pk).first()
            bank_account.delete()
            return Response({'message': 'Cuenta eliminada correctamente!'}, status = status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado una cuenta con estos datos'}, status = status.HTTP_400_BAD_REQUEST)

