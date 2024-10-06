from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from.models import Post

# Create your views here.
class Home(ListView):
    model = Post
    template_name = 'home.html'

class blog_article_content(DetailView):
    model = Post
    template_name = 'blog_article_content.html'

class create_post(CreateView):
    model = Post
    template_name = 'create_post.html'
    fields = '__all__'

class login(CreateView):
    model = Post
    template_name = 'login.html'
    fields ='__all__'