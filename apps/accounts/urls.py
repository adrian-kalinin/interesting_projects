from django.urls import path, include

from .views import CreateUserView


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('create/', CreateUserView.as_view(), name='signup')
]
