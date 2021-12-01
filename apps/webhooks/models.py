from django.db import models

from apps.accounts.models import User


class WebhookConfig(models.Model):
    url = models.CharField(max_length=240)
    owner = models.ForeignKey(User, related_name='webhook_configs', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Webhook Config'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.url} ({self.owner.username})'
