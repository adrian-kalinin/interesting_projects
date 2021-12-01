from rest_framework import serializers

from .models import ProjectEntry


class ProjectEntrySerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ProjectEntry
        fields = ('name', 'description', 'link', 'rating', 'owner')
