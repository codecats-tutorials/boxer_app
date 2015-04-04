from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from mongoengine import DoesNotExist
from mongoengine.django.auth import User
from rest_framework.views import APIView
from userprofile.documents import UserProfile
from userprofile.serializers import LoginSerializer
from userprofile.views.authentication_mixin import AuthenticationMixin

__author__ = 't'

class LoginView(APIView, AuthenticationMixin):

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_authentication_representation(request))

    def post(self, request, *args, **kwargs):
        errors = {'loginError': []}
        user = None
        return JsonResponse(LoginSerializer().to_representation(user))
        try:
            user = UserProfile.objects.get(email=request.DATA.get('email'))
        except DoesNotExist:
            errors['loginError'].append('User not found!')
        if user is not None and user.check_password(request.DATA.get('password')):
            login(request, user)
            #request.session.set_expiry(60 * 60 * 1)
        auth = self.get_authentication_representation(request)
        auth.update(errors)
        return JsonResponse(auth)
