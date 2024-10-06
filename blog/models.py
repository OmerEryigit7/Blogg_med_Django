from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateField(default=timezone.now())

    def __str__(self):
        return str(self.title) + '  -  ' + str(self.author)
# Create your models here.
