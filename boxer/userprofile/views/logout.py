from django.contrib.auth import logout
from django.http import JsonResponse
from rest_framework.views import APIView
from userprofile.views.authentication_mixin import AuthenticationMixin

__author__ = 't'


class LogoutView(APIView, AuthenticationMixin):

    def get(self, request, *args, **kwargs):
        logout(request)
        return JsonResponse(self.get_authentication_representation(request))