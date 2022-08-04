from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]

# https://docs.djangoproject.com/en/4.0/topics/auth/default/