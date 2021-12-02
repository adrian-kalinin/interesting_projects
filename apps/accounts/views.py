from rest_framework import permissions, serializers
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from django.db import models
from typing import List

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):
    model: models.Model = get_user_model()
    serializer_class: serializers.BaseSerializer = UserSerializer
    permission_classes: List[permissions.BasePermission] = [permissions.AllowAny]
