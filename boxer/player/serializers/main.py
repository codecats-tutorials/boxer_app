from rest_framework import serializers
from organizations.const import ORGANIZATIONS
from player.documents import Player

__author__ = 't'

class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=200)
    avatar = serializers.CharField(allow_null=True)
    birthdate = serializers.DateField(input_formats=['%Y/%m/%d'], required=False)
    champion = serializers.MultipleChoiceField(allow_null=True, choices=ORGANIZATIONS, required=False)



    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.surname = validated_data.get('surname', instance.surname)
        instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.champion = validated_data.get('champion', instance.champion)
        #instance.birthdate = validated_data.get('birthdate', instance.birthdate)
        return instance

    def create(self, validated_data):
        return Player(**validated_data)
