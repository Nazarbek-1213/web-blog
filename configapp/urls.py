from django.urls import path
from .views import *
urlpatterns=[
path('post/new',CreatePostView.as_view(),name='Post_new'),
    path('',BlogListView.as_view(),name='index'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='Post_detail'),
    path('post/<int:pk>/edit',PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete',PostDeleteView.as_view(),name='delete_post')


 ]