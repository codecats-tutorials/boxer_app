from django.http import JsonResponse
from rest_framework.views import APIView
from organizations.const import ORGANIZATIONS
from player.documents import Player

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        organizations, org_objects = (dict(ORGANIZATIONS).keys(), [])
        taken_orgs = map(lambda x: x.values()[0], Player.organizations()['result'])
        for org in organizations:
            org_objects.append({
                'name': org,
                'available': not org in taken_orgs
            })
        return JsonResponse(org_objects, safe=False)