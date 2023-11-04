from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=7)
    artist = models.CharField(max_length=226)
    year = models.CharField(max_length=4)
    views = models.IntegerField()
    features = models.TextField()
    lyrics = models.TextField()
    language_cld3 = models.CharField(max_length=3)
    language_ft = models.CharField(max_length=3)
    language = models.CharField(max_length=3)
