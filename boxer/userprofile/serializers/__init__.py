from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        data = super(LoginSerializer, self).validate(attrs)

        return data
    def to_representation(self, instance):
        return {
            'email': 'TT',
            'isAuthenticated': True,
            'id': 12,
        }