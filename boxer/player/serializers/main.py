from rest_framework import serializers

__author__ = 't'

class PlayerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    surname = serializers.CharField(max_length=200)


