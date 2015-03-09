from django.contrib.auth import login
from django.http import HttpResponse, JsonResponse
from mongoengine.django.auth import User
from rest_framework.views import APIView
from userprofile.documents import UserProfile
from userprofile.views.authentication_mixin import AuthenticationMixin

__author__ = 't'

class LoginView(APIView, AuthenticationMixin):

    def get(self, request, *args, **kwargs):
        return JsonResponse(self.get_authentication_representation(request))

    def post(self, request, *args, **kwargs):
        user = UserProfile.objects.get(email=request.DATA.get('email'))
        if user.check_password(request.DATA.get('password')):
            login(request, user)
            #request.session.set_expiry(60 * 60 * 1)
        return JsonResponse(self.get_authentication_representation(request))
