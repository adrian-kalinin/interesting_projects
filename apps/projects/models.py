from django.db import models


class ProjectEntry(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    link = models.CharField(max_length=240, unique=True)
    rating = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project Entry'
        verbose_name_plural = 'Project Entries'

        ordering = ['-created_at']

        constraints = [
            models.CheckConstraint(
                check=models.Q(rating__range=(1, 5)),
                name='check_rating_range'
            )
        ]

    def __str__(self):
        return self.name  # f'{self.name} (self.link)'
