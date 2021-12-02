from django.db import models
from typing import List

from apps.accounts.models import User


class ProjectEntry(models.Model):
    name: models.Model = models.CharField(max_length=120)
    description: models.Model = models.TextField()
    link: models.Model = models.CharField(max_length=240, unique=True)
    rating: models.Model = models.IntegerField()
    owner: models.ForeignKey = models.ForeignKey(User, related_name='project_entries', on_delete=models.CASCADE)

    created_at: models.Model = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at: models.Model = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name: str = 'Project Entry'
        verbose_name_plural: str = 'Project Entries'

        ordering: List[str] = ['-created_at']

        constraints: List[models.CheckConstraint] = [
            models.CheckConstraint(
                check=models.Q(rating__range=(1, 5)),
                name='check_rating_range'
            )
        ]

    def __str__(self) -> str:
        return f'{self.name} ({self.id})'
