from rest_framework import serializers

from .models import WebhookConfig


class WebhookConfigSerializer(serializers.ModelSerializer):
    url = serializers.URLField()
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = WebhookConfig
        fields = ['url', 'owner']
