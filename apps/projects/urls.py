from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProjectEntryViewSet


router = DefaultRouter()
router.register('project-entries', ProjectEntryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
