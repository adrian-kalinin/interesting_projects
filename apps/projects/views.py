from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response

from .models import ProjectEntry
from .serializers import ProjectEntrySerializer
from apps.accounts.permissions import IsOwnerOrReadOnly


class ProjectEntryViewSet(viewsets.ModelViewSet):
    queryset = ProjectEntry.objects.all()
    serializer_class = ProjectEntrySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at']

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def create(self, request, *args, **kwargs):
        project_entry = ProjectEntry.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            link=request.data['link'],
            rating=request.data['rating'],
            owner=request.user
        )

        serializer = self.get_serializer(project_entry)
        return Response(serializer.data)
