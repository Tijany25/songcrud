from email.policy import default
from django.db import models
from datetime import datetime

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=40)
    date_released = models.DateField(default=datetime.today)
    likes = models.CharField(max_length=40)
    artiste_id = models.ForeignKey(Artiste, on_delete=models.CASCADE)

class Lyric(models.Model):
    content = models.CharField(max_length=4000)
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
