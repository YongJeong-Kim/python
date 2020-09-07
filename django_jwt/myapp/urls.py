from django.urls import path
from . import views

urlpatterns = [
    # path('posts/', views.posts, name='posts'),
    path('posts/', views.PostApiView.as_view(), name='posts'),
]