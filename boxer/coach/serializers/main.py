from rest_framework import serializers
from coach.documents import Coach
from player.serializers.main import PlayerSerializer

__author__ = 't'

class CoachSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField()
    surname = serializers.CharField()
    rate = serializers.IntegerField(min_value=0, max_value=5, allow_null=True, required=False)
    players = serializers.ListField(allow_null=True)

    def __init__(self, *args, **kwargs):
        if 'data' in kwargs:
            kwargs['data']['players'] = kwargs['data'].get('selectedPlayers')

        super(CoachSerializer, self).__init__(*args, **kwargs)

    def update(self, instance, validated_data):
        for v in validated_data:
            setattr(instance, v, validated_data.get(v))
        return instance

    def create(self, validated_data):
        return Coach(**validated_data)

    def to_representation(self, instance):
        represent = super(CoachSerializer, self).to_representation(instance)
        data = map(lambda x: PlayerSerializer(x).data, represent['players'])
        represent['players'] = data
        return represent