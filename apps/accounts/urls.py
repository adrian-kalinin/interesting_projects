from django.urls import path, include
from rest_framework.authtoken import views

from .views import CreateUserView


urlpatterns = [
    path('', include('rest_framework.urls')),
    path('token/', views.obtain_auth_token, name='token'),
    path('signup/', CreateUserView.as_view(), name='signup')
]
