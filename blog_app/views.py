from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView,CreateView
from django.urls import reverse_lazy
from .models import Post


class Home(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "blog_app/blogs.html"
    paginate_by = 3
    ordering = ['-created_at']  # Replace 'created_at' with the field you want to order by


class Post_DetailView(DetailView):
    model = Post
    template_name = "blog_app/detailview.html"


class Post_UpdateView(UpdateView):
    model = Post
    fields = ["title","content","author","image"]
    template_name = "blog_app/updateview.html"
    success_url =reverse_lazy('Home') 


class Post_DeleteView(DeleteView):
    model = Post
    template_name = "blog_app/deleteview.html"
    success_url =reverse_lazy('Home') 


class Post_CreateView(CreateView):
    model = Post
    template_name = 'blog_app/createview.html'
    fields = ["title","content","author","image"]
    success_url = reverse_lazy('Home')
