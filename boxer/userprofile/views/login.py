from time import sleep
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
        serializer = LoginSerializer(data=request.DATA)
        if serializer.is_valid():
            serializer.login_user(request)
        return JsonResponse(serializer.to_representation(request.user, request.DATA))
