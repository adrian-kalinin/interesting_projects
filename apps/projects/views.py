from rest_framework import viewsets, permissions, filters, serializers
from rest_framework.response import Response
from rest_framework.request import Request
from typing import List

from .models import ProjectEntry
from .serializers import ProjectEntrySerializer
from apps.accounts.permissions import IsOwnerOrReadOnly


class ProjectEntryViewSet(viewsets.ModelViewSet):
    queryset = ProjectEntry.objects.all()
    serializer_class: serializers.BaseSerializer = ProjectEntrySerializer
    filter_backends: List[filters.BaseFilterBackend] = [filters.OrderingFilter]
    ordering_fields: List[str] = ['rating', 'created_at']

    permission_classes: List[permissions.BasePermission] = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def create(self, request: Request, *args, **kwargs) -> Response:
        project_entry: ProjectEntry = ProjectEntry.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            link=request.data['link'],
            rating=request.data['rating'],
            owner=request.user
        )

        serializer = self.get_serializer(project_entry)
        return Response(serializer.data)
