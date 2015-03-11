# -*- coding: utf-8 -*-

from rest_framework import serializers
from organizations.const import ORGANIZATIONS
from player.documents import Player

__author__ = 't'

class PlayerSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=200)
    avatar = serializers.CharField(allow_null=True)
    birthdate = serializers.DateTimeField(required=False, allow_null=True)
    champion = serializers.MultipleChoiceField(required=False, allow_null=True, choices=ORGANIZATIONS)
    reach = serializers.IntegerField(required=False, allow_null=True, max_value=250, min_value=150)
    height = serializers.IntegerField(required=False, allow_null=True, max_value=250, min_value=150)
    description = serializers.CharField(required=False, allow_null=True, max_length=4096)
    division = serializers.ChoiceField(
        allow_null=True, required=False,
        choices=Player.DIVISIONS
    )
    stance = serializers.CharField(required=False, allow_null=True, max_length=20)

    def update(self, instance, validated_data):
        for v in validated_data:
            setattr(instance, v, validated_data.get(v))
        return instance

    def create(self, validated_data):
        return Player(**validated_data)

    def to_representation(self, instance):
        represent = super(PlayerSerializer, self).to_representation(instance)
        if 'champion' in represent:
            represent['champion'] = list(represent['champion'])
        if 'division' in  represent:
            represent['division'] = {'value': represent['division']}
        return represent