from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Activity(models.Model):
    Activityname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    vote_score = models.CharField(max_length=100)
