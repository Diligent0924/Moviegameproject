from rest_framework import serializers
from .models import MovieCards, BossCards, BossSkills

class BossCardsSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = BossCards
        fields = "__all__"