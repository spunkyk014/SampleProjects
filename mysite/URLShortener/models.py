from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
import datetime

# Create your models here.

class URLEntry(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    original_url = models.URLField(max_length=300)
    shortened_url = models.URLField()    
    created_date = models.DateTimeField('date created')
    
    def __str__(self):
        return self.original_url
    
    def Username(self):
        return username    
    
    def ShortenedURL(self):
        return shortened_url   

    def CreatedDate(self):
        return created_date

    def get_absolute_url(self):
        return reverse('URLShortener:userurls', kwargs={'pk': self.username})