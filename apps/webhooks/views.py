from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .models import WebhookConfig
from .serializers import WebhookConfigSerializer


class WebhookConfigViewSet(viewsets.ModelViewSet):
    serializer_class = WebhookConfigSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WebhookConfig.objects.filter(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        project_entry = WebhookConfig.objects.create(
            url=request.data['url'],
            owner=request.user
        )

        serializer = self.get_serializer(project_entry)
        return Response(serializer.data)