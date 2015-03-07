from rest_framework import serializers
from player.documents import Player

__author__ = 't'
class MultipleOf:
    def __init__(self, base):
        self.base = base

    def __call__(self, value):
        # if value % self.base != 0:
        message = 'This field must be a multiple of %s.' % self.base
        raise serializers.ValidationError(message)


    def set_context(self, serializer_field):
        # Determine if this is an update or a create operation.
        # In `__call__` we can then use that information to modify the validation behavior.
        self.is_update = serializer_field.parent.instance is not None



class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=200, validators=[MultipleOf('abc')])
    date_dele = serializers.DateField(input_formats=['%Y/%m/%d'])


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        return instance

    def create(self, validated_data):
        return Player(**validated_data)
