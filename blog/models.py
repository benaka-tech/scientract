from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.urls import reverse
from django.db import models
from django.utils.text import slugify


import misaka

from django.contrib.auth import get_user_model
User = get_user_model()


from django import template
register = template.Library()


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    moderation = models.BooleanField(default=False)
    document = models.FileField(upload_to='documents/' ,null=True, blank=True,default='')
    confirm=models.BooleanField(default=False)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Announce(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    moderation = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class moderation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    moderation = models.BooleanField(default=False)   