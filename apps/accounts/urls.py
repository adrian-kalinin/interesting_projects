from django.urls import path, include, URLPattern
from rest_framework.authtoken import views
from typing import List

from .views import CreateUserView


urlpatterns: List[URLPattern] = [
    path('', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token, name='token'),
    path('signup/', CreateUserView.as_view(), name='signup')
]
