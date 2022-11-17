from django.db import models
from django.conf import settings
# Create your models here.


# 그냥 평범한 카드
class Card(models.Model):
    movie_id = models.IntegerField(primary_key=True)
    movie_type = models.CharField(max_length=100)
    is_show = models.BooleanField(default=False)

class NormalCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    attack_damage = models.IntegerField()
    hp = models.IntegerField()
# 특수 유닛이 있는 카드
class UniqueCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    attack_damage = models.IntegerField()
    hp = models.IntegerField()

# 보스 카드
class BossCard(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE) 
    name = models.CharField(max_length=200)
    poster_path = models.CharField(max_length=200)
    attack_damage = models.IntegerField()
    hp = models.IntegerField()

# 만약 type이 unique거나 boss일 경우에만 들어갈 수 있도록 하면 된다.
class Skill(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    skill_type = models.CharField(max_length=100)
    skill_range = models.IntegerField() # 회복이든 뭐든~
    skill_comment = models.CharField(max_length=100, default = "이 카드는 평범한 카드입니다...")
