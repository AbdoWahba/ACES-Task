from django.db import models

# Create your models here.
class About(models.Model):
    about_aces=models.CharField(max_length=1000)
    mission=models.CharField(max_length=1000)
    vision=models.CharField(max_length=1000)
    youtube_link=models.CharField(max_length=1000)
    accepted=models.IntegerField(default=0)