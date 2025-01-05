from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from .models import Post, Category, Comment
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect

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
    fields = ['title', 'body', 'categories']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        post = self.get_object()

        if post.author != request.user:
            messages.error(request, "Hva faen")
            return HttpResponseRedirect(self.success_url)
        
        return super().dispatch(request, *args, **kwargs)
    
class comment(CreateView):
    model = Comment
    fields = ['body']
    template_name = 'newcomment.html'

    def get_success_url(self):
        return reverse_lazy('artikkel', kwargs={'pk': self.object.post.pk})

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['pk'])
        return super().form_valid(form)


def economy_posts(request):
    posts = Post.objects.filter(categories__name='Økonomi')
    return render(request, 'økonomi.html', {'object_list': posts})

def school_posts(request):
    posts = Post.objects.filter(categories__name='Skole')
    return render(request, 'skole.html', {'object_list': posts})

def it_posts(request):
    posts = Post.objects.filter(categories__name='IT')
    return render(request, 'it.html', {'object_list': posts})

def technology_posts(request):
    posts = Post.objects.filter(categories__name='Teknologi')
    return render(request, 'teknologi.html', {'object_list': posts})

def other_posts(request):
    posts = Post.objects.filter(categories__name='Annet')
    return render(request, 'annet.html', {'object_list': posts})

def user_profile(request, username):
    pass