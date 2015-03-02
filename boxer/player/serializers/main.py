from rest_framework import serializers
from player.documents import Player

__author__ = 't'

class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=200)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        return instance

    def create(self, validated_data):
        return Player(**validated_data)


