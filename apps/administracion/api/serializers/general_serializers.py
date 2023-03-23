from apps.administracion.models import Position, Category, Bank
from rest_framework import serializers



class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_date', 'deleted_date', 'state',)

class PositionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Position
        exclude = ('created_date', 'deleted_date', 'place_number2')

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'