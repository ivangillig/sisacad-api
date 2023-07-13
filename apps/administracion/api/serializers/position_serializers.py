from apps.administracion.api.serializers.general_serializers import PositionSerializer
from apps.administracion.models import Position_Teacher
from apps.docentes.api.serializers.teacher_serializers import TeacherSerializer
from rest_framework import serializers

class Position_TeacherSerializer(serializers.ModelSerializer):
    #position = PositionSerializer()
    #teacher = TeacherSerializer()
    class Meta:
        model= Position_Teacher
        exclude = ('created_date', 'deleted_date', 'delete_motive', 'state')


    def to_representation(self, instance):
        return{
            'id': instance.id,
            'position': instance.position.id if instance.position.id is not None else '',
            'place_number1': instance.position.place_number1,
            'category': instance.position.category.category_id,
            'teacher': instance.teacher.id,
            'first_name': instance.teacher.first_name,
            'first_lastname': instance.teacher.first_lastname,
            'position_type': instance.position_type,
            'condition': instance.condition,
        }
