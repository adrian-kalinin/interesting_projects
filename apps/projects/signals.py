from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework import serializers
from typing import Dict, List

from apps.projects.models import ProjectEntry
from apps.projects.serializers import ProjectEntrySerializer
from apps.webhooks.models import WebhookConfig

import httpx


@receiver(post_save, sender=ProjectEntry)
def creat_shopping_cart(sender: ProjectEntry, instance: ProjectEntry, **kwargs) -> None:
    serializer: serializers.BaseSerializer = ProjectEntrySerializer(instance)
    data: Dict = serializer.data

    webhooks: List[WebhookConfig] = WebhookConfig.objects.filter(owner=instance.owner)

    for webhook in webhooks:
        httpx.post(webhook.url, data=data)
