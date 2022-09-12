from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.socialloginmain, name="socialloginmain"),
    path('login/', views.sociallogin, name="sociallogin"),
]