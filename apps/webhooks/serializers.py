from rest_framework import serializers
from django.db import models
from typing import List

from .models import WebhookConfig


class WebhookConfigSerializer(serializers.ModelSerializer):
    url: serializers.Field = serializers.URLField()
    owner: serializers.Field = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model: models.Model = WebhookConfig
        fields: List[str] = ['url', 'owner']
