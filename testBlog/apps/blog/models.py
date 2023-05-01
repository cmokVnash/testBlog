from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = ('DF', 'Draft')
        PUBLISHED = ('PUB', 'Published')

    title = models.CharField(max_length=250, null=False, blank=False)
    
    slug = models.SlugField(max_length=250)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, name="blog_posts")
   
    publish = models.DateField(default=timezone.now)

    create = models.DateField(auto_now_add=True)
    
    update = models.DateField(auto_now=True)

    status = models.CharField(max_length=3,choices=Status.choices,default=Status.DRAFT)

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title
    