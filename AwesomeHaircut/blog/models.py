from datetime import datetime
from django.db import models
from django.utils import timezone

# Create your models here.


class BlogPost(models.Model):
    """
    Hopefully this class is all I need for a blog post.
    """
    title = models.CharField(max_length=70)
    # date = models.DateField()
    content = models.TextField()
    is_published = models.BooleanField()
    tags = [models.CharField(max_length=70)]
    date_published = models.DateTimeField(default=timezone.now)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title  
