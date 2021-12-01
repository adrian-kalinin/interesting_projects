from rest_framework import viewsets
from rest_framework import permissions

from .models import ProjectEntry
from .serializers import ProjectEntrySerializer
from apps.accounts.permissions import IsOwnerOrReadOnly


class ProjectEntryViewSet(viewsets.ModelViewSet):
    queryset = ProjectEntry.objects.all()
    serializer_class = ProjectEntrySerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
