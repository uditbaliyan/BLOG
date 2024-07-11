
from .forms import UserRegistrationForm
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class Home(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "blog_app/blogs.html"
    paginate_by = 3
    ordering = ['-created_at']  # Replace 'created_at' with the field you want to order by


class Post_DetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "blog_app/detailview.html"


class Post_UpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content", "image"]
    template_name = "blog_app/updateview.html"
    success_url = reverse_lazy('Home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class Post_DeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog_app/deleteview.html"
    success_url = reverse_lazy('Home')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class Post_CreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog_app/createview.html'
    fields = ["title", "content", "image"]
    success_url = reverse_lazy('Home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog_app/register.html', {'form': form})
