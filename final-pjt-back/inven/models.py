from django.db import models
from django.conf import settings

# Create your models here.
class Moviecount(models.Model):
    movie_id = models.IntegerField(primary_key=True)