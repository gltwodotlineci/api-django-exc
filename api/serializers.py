from rest_framework import serializers
from .models import Task, BatBoysGame, Event


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatBoysGame
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['name_event', 'month']

