from django.urls import path
from . import views

urlpatterns = [
    path('', views.dev1, name='dev1'),
]