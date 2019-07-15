# from __future__ import unicode_literals
# try:
#     from django.core.urlresolvers import reverse
# except ModuleNotFoundError:
#     from django.urls import reverse

from django.urls import reverse

from django.db import models
from django.utils import timezone

class Post(models.Model):
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

#scaffold
import generic_scaffold

class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    category = models.CharField(max_length=32)

    def get_absolute_url(self):
        return reverse(self.detail_url_name, args=[self.id])

    def __str__(self):
        return '{0} {1} {2}'.format(self.title, self.author, self.category)

