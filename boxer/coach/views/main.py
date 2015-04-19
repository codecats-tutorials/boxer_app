from time import sleep
from django.http import JsonResponse
from rest_framework.views import APIView
from coach.documents import Coach
from coach.serializers.main import CoachSerializer
from vote.documents import UserCoachVote

__author__ = 't'

class Main(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get('count'):
            response = {'count': Coach.objects().count()}
        elif kwargs.get('id', False):
            coach = Coach.objects().get(pk=kwargs.get('id'))
            vote = UserCoachVote.objects(coach=coach)
            coach.rate = vote[0].rate if vote.count() > 0 else None
            response = CoachSerializer(coach).data
        else:
            page = int(request.GET.get('page', 1))
            coaches = Coach.objects()[(page-1) * 5: page * 5]
            votes = UserCoachVote.objects(coach__in=coaches)
            for coach in coaches:
                for vote in votes:
                    if vote.coach == coach:
                        coach.rate = vote.rate
            response = {'data': map(lambda x: CoachSerializer(x).data, coaches)}

        return JsonResponse(response)


    def post(self, request, *args, **kwargs):

        serializer = CoachSerializer(data=request.DATA.copy())
        if serializer.is_valid():
            coach = serializer.save()
            coach.save()
            response = CoachSerializer(coach).data
        else:
            response = {'errors': serializer.errors}

        return JsonResponse(response)

    def put(self, request, *args, **kwargs):
        data = request.DATA.copy()
        serializer = CoachSerializer(data=request.DATA.copy())
        if serializer.is_valid():
            coach  = serializer.save()
            coach.save()
            response = CoachSerializer(coach).data
        else:
            data['errors']  = serializer.errors
            response = data

        return JsonResponse(response)

    def delete(self, request, *args, **kwargs):
        valid = False
        if request.user.is_authenticated():
            Coach.objects().get(pk=kwargs.get('id')).delete()
            valid |= True
        return JsonResponse({'valid': valid})