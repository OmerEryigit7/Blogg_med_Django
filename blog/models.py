from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(default=timezone.now)
    categories = models.ManyToManyField(Category, related_name='posts', default="Annet")

    def __str__(self):
        return str(self.title) + '  -  ' + str(self.author)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return '%s - %s - %s' % (self.post.title, self.comment_author, self.date)



# Create your models here.