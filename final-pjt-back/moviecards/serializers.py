from rest_framework import serializers
from .models import Card,NormalCard,UniqueCard,BossCard,UniqueSkill,BossSkill

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = "__all__"
class NormalCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = NormalCard
        fields = "__all__"



class UniqueSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UniqueSkill
        fields = "__all__"
        read_only_fields = ('card_id',)

class UniqueCardSerializer(serializers.ModelSerializer):
    skill_set = UniqueSkillSerializer(many=True, read_only=True)
    class Meta:
        model = UniqueCard
        fields = "__all__"
        read_only_fields = ('card_id',)

class BossSkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = BossSkill
        fields = "__all__"

class BossCardSerializer(serializers.ModelSerializer):
    bossskill_set = BossSkillSerializer(many=True, read_only=True)
    class Meta:
        model = BossCard
        fields = "__all__"

class normaldetailSerializer(serializers.ModelSerializer):
    normalcard_set = NormalCardSerializer(many=True,read_only=True)
    class Meta:
        model = Card
        fields = "__all__"

class UniquedetailSerializer(serializers.ModelSerializer):
    uniquecard_set = UniqueCardSerializer(many=True, read_only=True)
    class Meta:
        model = Card
        fields = "__all__" 

class BossdetailSerializer(serializers.ModelSerializer):
    bosscard_set = BossCardSerializer(many=True, read_only=True)
    class Meta:
        model = Card
        fields = "__all__"    

class plusSerializer(serializers.Serializer):
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
