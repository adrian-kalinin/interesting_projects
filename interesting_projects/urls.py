from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view

from django.views.generic import TemplateView


schema_view = get_schema_view(title='Interesting Projects API')

swagger_view = TemplateView.as_view(
    template_name='swagger.html',
    extra_context={'schema_url': 'openapi-schema'}
)


urlpatterns = [
    path('admin/', admin.site.urls),

    path('openapi-schema/', schema_view, name='openapi-schema'),
    path('swagger/', swagger_view, name='swagger'),

    path('projects/', include('apps.projects.urls'), name='projects'),
    path('auth/', include('apps.accounts.urls'), name='accounts')
]
