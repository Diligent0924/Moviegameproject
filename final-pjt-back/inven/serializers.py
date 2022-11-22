from rest_framework import serializers
from .models import Moviecount

class MovieCountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Moviecount
        fields = "__all__"

# class ArticleListSerializer(serializers.Serializer):