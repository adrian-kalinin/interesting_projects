from rest_framework import serializers

from .models import WebhookConfig


class WebhookConfigSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WebhookConfig
        fields = ['url', 'owner']
