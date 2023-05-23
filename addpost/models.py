from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.TextField()
    ingredients = models.TextField()
    body = models.TextField()
    # describe the project 
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self) :
        return (self.body)