from django.db import models
from django.utils import timezone

class Author(models.Model):
    nick = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nick

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title