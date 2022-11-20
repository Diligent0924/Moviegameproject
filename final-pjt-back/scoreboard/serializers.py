from rest_framework import serializers
from .models import Board, Comment, MovieCard


class BoardListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Board
        fields = '__all__'
        # fields = ('id', 'title', 'content', 'user', 'username')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('board',)

class MovieCardSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieCard
        fields = '__all__'
        read_only_fields = ('board',)

# class normaldetailSerializer(serializers.Serializer):
#     movieid = serializers.IntegerField()
#     movietype = serializers.CharField(max_length=100)
#     card_id = serializers.IntegerField()
#     name = serializers.CharField(max_length=200)
#     posterpath = serializers.CharField(max_length=200)
#     attackdamage = serializers.IntegerField()
#     hp = serializers.IntegerField()
#     skilltype = serializers.CharField(max_length=100)
#     skillrange = serializers.IntegerField() # 회복이든 뭐든~
#     skillcomment = serializers.CharField(max_length=100, default = "이 카드는 평범한 카드입니다...")

class BoardSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    moviecard_set = MovieCardSerializer(many=True, read_only=True)
    # card_detail = normaldetailSerializer(many=True, read_only=True)
    # comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Board
        fields = '__all__'
        # read_only_fields = ('movie_id', )