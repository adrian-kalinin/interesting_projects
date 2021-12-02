from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.projects.models import ProjectEntry
from apps.projects.serializers import ProjectEntrySerializer
from apps.webhooks.models import WebhookConfig

import httpx


@receiver(post_save, sender=ProjectEntry)
def creat_shopping_cart(sender, instance, **kwargs):
    serializer = ProjectEntrySerializer(instance)
    data = serializer.data

    webhooks = WebhookConfig.objects.filter(owner=instance.owner)

    for webhook in webhooks:
        httpx.post(webhook.url, data=data)
