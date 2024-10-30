from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from.models import Post
from django.urls import reverse_lazy

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class blog_article_content(DetailView):
    model = Post
    template_name = 'blog_article_content.html'

class create_post(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = ['title', 'body']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)