from django.apps import AppConfig


class ProjectsConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'apps.projects'

    def ready(self) -> None:
        import apps.projects.signals
