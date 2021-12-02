from rest_framework import viewsets, permissions, serializers
from rest_framework.response import Response
from rest_framework.request import Request

from .models import WebhookConfig
from .serializers import WebhookConfigSerializer


class WebhookConfigViewSet(viewsets.ModelViewSet):
    serializer_class: serializers.BaseSerializer = WebhookConfigSerializer
    permission_classes: List[permissions.BasePermission] = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WebhookConfig.objects.filter(owner=self.request.user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        project_entry = WebhookConfig.objects.create(
            url=request.data['url'],
            owner=request.user
        )

        serializer = self.get_serializer(project_entry)
        return Response(serializer.data)