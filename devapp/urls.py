from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='testbase'),
    path('dev1/', views.dev1, name='dev1'),
    path('dev2/', views.dev2, name='dev2'),
    path('dev3/', views.dev3, name='dev3'),
]