from rest_framework.routers import DefaultRouter
from django.urls import path, include, URLPattern
from typing import List

from .views import ProjectEntryViewSet


router: DefaultRouter = DefaultRouter()
router.register('', ProjectEntryViewSet)


urlpatterns: List[URLPattern] = [
    path('', include(router.urls))
]
