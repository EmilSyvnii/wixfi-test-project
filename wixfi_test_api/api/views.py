from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.models import User
from api.serializers import UserSerializer
from api.tasks import run_simple_task


@api_view(['GET'])
def Overview(request):
    json_data = {
        'q1': 1,
        'q2': 2,
    }
    return Response(json_data)


@api_view(['GET'])
def UserList(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def UserAdd(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET'])
def RunCeleryTask(request):
    run_simple_task()
    return Response('Run Celery task')



