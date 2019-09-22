from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:postId>/view/', views.postView, name='post-detail'),
    path('post/add/', views.postCreate, name='post-create'),
    path('post/<int:pk>/update/', views.postUpdate, name='post-update'),
    path('post/<int:pk>/delete/', views.postDelete, name='post-delete'),
]
