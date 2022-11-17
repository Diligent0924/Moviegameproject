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