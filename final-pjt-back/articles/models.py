from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    user = models.CharField(max_length=100)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie_id = models.IntegerField() # 영화정보를 가져와야함.
    stage = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

