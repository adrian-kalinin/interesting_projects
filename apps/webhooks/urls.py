from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import WebhookConfigViewSet


router = DefaultRouter()
router.register('', WebhookConfigViewSet, 'webhook-configs')


urlpatterns = [
    path('', include(router.urls))
]
