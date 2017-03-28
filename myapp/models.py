from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    Activityname = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    vote_score = models.CharField(max_length=100)

    def __unicode__(self):
		return "id: %s"%(self.Activityname)


class Vote(models.Model):
    DAY_CHOIE = [(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday')]
    activity = models.ForeignKey("Activity" ,on_delete=models.SET_NULL, blank=True,null=True)

    #days = models.BigIntegerField(verbose_name='days:', choices=DAY_CHOIE)
    days = models.CharField(max_length=50)
    user = models.CharField(max_length=50, null=True)
    def __unicode__(self):
		return "id: %s"%(self.activity)
