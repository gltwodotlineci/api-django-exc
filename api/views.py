from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer, GameSerializer, EventSerializer
from .models import Task, BatBoysGame, Event
from rest_framework import viewsets # Second Half
from django.contrib.auth.models import Permission, User
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from users.models import AuthenticTokenUs, AuthenticateTwo

#from . import permissions


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/tast-list/',
        'Detail View': '/tast-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/tast-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }

    return Response(api_urls)


@api_view(['GET', 'POST'])
def tasklist(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def taskDetail(request, pk):
    task = Task.objects.get(id=pk)
    print(request.user)
    if request.method == 'GET':
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    user = request.user
    if user.is_anonymous:
        return Response("You can't modify the API", status=status.HTTP_401_UNAUTHORIZED)

    if request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#       ----- SERIALIZER WITH THE ViewSets METHODS ------

class BatGameViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = BatBoysGame.objects.all()
        serializer = GameSerializer(queryset, many=True)
        #permission_obj = [permissions.IsAthenticatedOrReadOnly]
        return Response(serializer.data)

    def retrieve(self, request, pk):
        queryset = BatBoysGame.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GameSerializer(game)
        #permission_obj = [permissions.IsAthenticatedOrReadOnly]
        return Response(serializer.data)

    def create(self, request):
        serializer = GameSerializer(data=request.data)
        #permission_obj = [permissions.IsAthenticatedOrReadOnly]
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        queryset = BatBoysGame.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        serializer = GameSerializer(game, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        queryset = BatBoysGame.objects.all()
        game = get_object_or_404(queryset, pk=pk)
        game.delete()
        return Response(('deleted'), status=status.HTTP_200_OK)

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        #elif self.action in ['create']:
            #permission_classes = Permission.objects.filter(request.user)
        else:
            permission_classes = [AuthenticTokenUs]
        return [permission() for permission in permission_classes]


class EventViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

    def retreive(self, request, pk):
        queryset = Event.objects.all()
        event = get_object_or_404(queryset, pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def create(self, request):
        serializer = EventSerializer(data=request.data)
        #permission_obj = [permissions.IsAthenticatedOrReadOnly]
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    pass

    def get_permission(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [AuthenticateTwo]
            return [permission() for permission in permission_classes]

