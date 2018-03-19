from django.db import models

# Create your models here.


class BlogPost(models.Model):
    """
    Hopefully this class is all I need for a blog post.
    """
    title = models.CharField(max_length=70)
    date = models.DateField()
    content = models.TextField()
    ispublished = models.BooleanField()

    def __str__(self):
        return self.title


class Tag(models.Model):
    """
    hmm what
    """
    pass
