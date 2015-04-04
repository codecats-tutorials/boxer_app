from django.http import JsonResponse
from rest_framework.views import APIView

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated() == False:
            return JsonResponse([], safe=False)
        return JsonResponse(['BOXERS'], safe=False)
