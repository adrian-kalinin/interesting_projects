from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import models
from typing import Tuple


User: models.Model = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password: serializers.Field = serializers.CharField(write_only=True)

    def create(self, validated_data: dict) -> User:
        user: User = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model: models.Model = User
        fields: Tuple[str] = ('id', 'username', 'password',)
