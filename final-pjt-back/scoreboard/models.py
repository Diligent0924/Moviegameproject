from django.db import models
from django.conf import settings

# Create your models here.
class Board(models.Model):
    stage = models.IntegerField()
    user = models.CharField(max_length=100)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class MovieCard(models.Model): # 모델필드를 밖에 빼놓고 사용
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    movietype = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    posterpath = models.CharField(max_length=200)
    attackdamage = models.IntegerField()
    hp = models.IntegerField()
    skillcomment = models.CharField(max_length=100, default = "이 카드는 평범한 카드입니다...")

class Comment(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    user = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

