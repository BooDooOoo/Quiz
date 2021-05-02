from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .models import Polls, Users
from .serializers import PollsSerializer, UserChoiceSerializer, PollQuestionsSerializer, CompletedPollsSerializer
from datetime import datetime, timedelta
from rest_framework.permissions import AllowAny


def index(request):
    print(request.POST)
    return render(request, 'polls/index.html')


def completed_polls_view(request):
    return render(request, 'polls/completed_polls.html')


@api_view(['GET'])
def test(request):
    polls = Polls.objects.all()
    serializer = PollsSerializer(polls, many=True)
    response = Response(serializer.data)

    if 'user' in request.COOKIES:
        print(request.COOKIES)
    else:
        user = Users.objects.create()
        response.set_cookie('user', value=user.id, expires=datetime.now() + timedelta(days=30))
        print(request.COOKIES)

    return response


@api_view(['GET'])
def get_questions(request, pk):
    poll_questions = Polls.objects.get(pk=pk)
    serializer = PollQuestionsSerializer(poll_questions)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((AllowAny,))
def user_choices(request):

    serializer = UserChoiceSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def completed_polls(request):
    if 'user' in request.COOKIES:
        user = request.COOKIES['user']
        polls = Polls.objects.filter(questions__user_choice__user=user).distinct()

        serializer = CompletedPollsSerializer(polls, many=True)
        return Response(serializer.data)
