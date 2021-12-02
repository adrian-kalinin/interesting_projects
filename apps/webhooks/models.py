from django.db import models
from typing import List

from apps.accounts.models import User


class WebhookConfig(models.Model):
    url: models.Field = models.CharField(max_length=240)
    owner: models.ForeignKey = models.ForeignKey(User, related_name='webhook_configs', on_delete=models.CASCADE)

    created_at: models.Field = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at: models.Field = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = 'Webhook Config'
        ordering: List[str] = ['-created_at']

    def __str__(self) -> str:
        return f'{self.url} ({self.owner.username})'
