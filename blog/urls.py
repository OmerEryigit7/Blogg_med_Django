"""
URL configuration for django_blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import Home
from .views import blog_article_content
from .views import create_post
from .views import economy_posts, school_posts, it_posts, technology_posts, other_posts, PostDeleteView, user_profile

urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('artikkel/<int:pk>', blog_article_content.as_view(), name="blog_article_content"),
    path('nyttinnlegg/', create_post.as_view(), name='create_post'),
    path('økonomi/', economy_posts, name="økonomi"),
    path('skole/', school_posts, name="skole"),
    path('it/', it_posts, name="it"),
    path('teknologi/', technology_posts, name="teknologi"),
    path('alle_innlegg/', other_posts, name="annet"),
    path('slett_innlegg/<int:pk>/', PostDeleteView.as_view(), name="delete"),
    path('profil/<str:username>/', user_profile, name="profil")
]
