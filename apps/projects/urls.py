from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ProjectEntryViewSet


router = DefaultRouter()
router.register('', ProjectEntryViewSet)


urlpatterns = [
    path('', include(router.urls))
]
