from django.apps import AppConfig


class WebhooksConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'apps.webhooks'
