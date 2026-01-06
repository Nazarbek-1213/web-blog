from django.contrib.admin.utils import model_ngettext
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, ListView
from .models import  *
from django.urls import reverse_lazy

class BlogListView(ListView):
    model =Post
    template_name = 'index.html'

class BlogDetailView(DetailView):
    model=Post
    template_name = 'Post_detail.html'

class CreatePostView(CreateView):
    model=Post
    template_name = 'Post_new.html'
    fields = ['title','author','body']

class PostUpdateView(UpdateView):
    model=Post
    template_name = 'post_edit.html'
    fields =['title','body']

class PostDeleteView(DeleteView):
    model=Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')
    fields=['title','author','body']

class PostListView(ListView):
    model=Post
    template_name = 'search_post.html'




