from rest_framework.routers import DefaultRouter
from django.urls import path, include, URLPattern
from typing import List

from .views import WebhookConfigViewSet


router: DefaultRouter = DefaultRouter()
router.register('', WebhookConfigViewSet, 'webhook-configs')


urlpatterns: List[URLPattern] = [
    path('', include(router.urls))
]
