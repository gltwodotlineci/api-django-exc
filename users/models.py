from django.db import models
from django.contrib.auth.models import AbstractUser

from rest_framework import permissions
from rest_framework.views import APIView


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

class AuthenticateTwo(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated()

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class AuthenticateTwo(APIView):

     def get_queryset(self):
        # after get all products on DB it will be filtered by its owner and return the queryset
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset

