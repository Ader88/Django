from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_list, name='posts_list'),
    path('<int:pk>/', views.post_details, name='post_details'),
    path('authors/', views.authors_list, name='authors_list'),
    path('author/<int:pk>/', views.author_details, name='author_details'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_author/', views.add_author, name='add_author'),
]