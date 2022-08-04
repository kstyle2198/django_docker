from django.urls import path
from . import views


urlpatterns = [
    # path('', views.blog),
    path('', views.PostList.as_view(), name="post_list"),
    path('<slug:slug>/', views.DetailView.as_view(), name="post_detail"),
]