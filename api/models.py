from django.db import models
from users.models import CustomUser

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.title


class BatBoysGame(models.Model):
    nb_participants = models.IntegerField()
    level = models.CharField(max_length=15)
    new_game = models.BooleanField(default=False, blank=True, null=False)
    #author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.level


class Event(models.Model):
    name_event = models.CharField(max_length=45)
    month = models.CharField(max_length=10)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name_event

