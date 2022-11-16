from django.db import models
from django.conf import settings
# Create your models here.
class MovieCards(models.Model):
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    attack_damage = models.IntegerField()
    hp = models.IntegerField()

class BossCards(models.Model):
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    attack_damage = models.IntegerField()
    hp = models.IntegerField()

class BossSkills(models.Model):
    boss_id = models.ForeignKey(BossCards, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=100)
    skill_range = models.IntegerField() # 회복이든 뭐든~
    skill_comment = models.CharField(max_length=100, default = "이 카드는 평범한 카드입니다...")
