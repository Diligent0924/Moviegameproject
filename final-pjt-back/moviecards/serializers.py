from rest_framework import serializers
from .models import Card,NormalCard,UniqueCard,BossCard,Skill

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
class NormalCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = NormalCard
        fields = "__all__"

class UniqueCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = UniqueCard
        fields = "__all__"

class BossCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = BossCard
        fields = "__all__"
class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = "__all__"

class normaldetailSerializer(serializers.Serializer):
    movieid = serializers.IntegerField()
    movietype = serializers.CharField(max_length=100)
    card_id = serializers.IntegerField()
    name = serializers.CharField(max_length=200)
    posterpath = serializers.CharField(max_length=200)
    attackdamage = serializers.IntegerField()
    hp = serializers.IntegerField()
    skilltype = serializers.CharField(max_length=100)
    skillrange = serializers.IntegerField() # 회복이든 뭐든~
    skillcomment = serializers.CharField(max_length=100, default = "이 카드는 평범한 카드입니다...")