from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework import permissions

class CustomUser(AbstractUser):
    is_staff = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=False)
    frist_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)


class AuthenticTokenUs(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return any([
                all([
                    request.user.is_staff,
                ]),
                request.user.is_superuser
            ])
        else:
            return False

    #def can_update_delete(self, request, view):
        #if request.user.is_authenticated

