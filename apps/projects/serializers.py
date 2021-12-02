from rest_framework import serializers
from django.db import models
from typing import Tuple

from .models import ProjectEntry


class ProjectEntrySerializer(serializers.ModelSerializer):
    rating: serializers.Field = serializers.IntegerField(min_value=1, max_value=5)
    owner: serializers.Field = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model: models.Model = ProjectEntry
        fields: Tuple[str] = ('name', 'description', 'link', 'rating', 'owner')
