from django.contrib.auth import login
from mongoengine import DoesNotExist
from rest_framework import serializers
from userprofile.documents import UserProfile


class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def login_user(self, request):
        data = self.validated_data

        try:
            user = UserProfile.objects.get(email=data.get('email'))
        except DoesNotExist:
            self._errors['General'] = ['User or password incorrect!']
        else:
            if user.check_password(data.get('password')):
                login(request, user)
                #request.session.set_expiry(60 * 60 * 1)
            else:
                self._errors['General'] = ['User or password incorrect!']


    def to_representation(self, instance, data=None):
        data = {'email': instance.email} if data is None else data
        return {
            'email': data.get('email'),
            'isAuthenticated': instance.is_authenticated(),
            'id': unicode(instance.pk),
            'errors': self.errors,
        }