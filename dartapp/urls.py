from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_statement_info, name="dart"),
]