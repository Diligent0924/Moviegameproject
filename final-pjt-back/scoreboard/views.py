from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import BoardListSerializer,BoardSerializer, CommentSerializer
from .models import Board, Comment, MovieCard
from moviecards.models import Card
from accounts.models import User
from inven.models import Moviecount

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def scoreboard_list(request):
    if request.method == 'GET': # 전체데이터확인
        articles = Board.objects.raw('select * from scoreboard_board order by id')
        serializer = BoardListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # 마지막에 데이터를 추가한 후에 해당 유저를 탈퇴처리 시킨다.
        data = request.data
        board = Board(stage=data['stage'],user=data['user'], title=data['title'], content=data['content'])
        board.save()
        # 해당 카드를 세부정보에 표현하는 방식..!
        for movie_id in data["movie_id"]:
            card = Card.objects.raw(f'select * from moviecards_card where movieid = {movie_id}')
            result = Card.objects.raw(f'select * from (select * from moviecards_card where movieid = {card[0].movieid} )as s1 join moviecards_{card[0].movietype}card as s2 on s1.movieid = s2.card_id left join moviecards_uniqueskill as s3 on s1.movieid = s3.card_id')
            if card[0].movietype == 'normal':
                moviecard = MovieCard(board=board, movie_id=result[0].movieid, movietype=result[0].movietype, name = result[0].name, posterpath=result[0].posterpath, attackdamage=result[0].attackdamage, hp=result[0].hp)            
            else:
                moviecard = MovieCard(board=board, movie_id=result[0].movieid, movietype=result[0].movietype, name = result[0].name, posterpath=result[0].posterpath, attackdamage=result[0].attackdamage, hp=result[0].hp, skillcomment=result[0].skillcomment)            
            moviecard.save()
            # 카드들의 아이디 정보를 INVEN에서 가져간다. => 추천 알고리즘을 위해서 필요함
            movie_count = Moviecount(movie_id=result[0].movieid)
            movie_count.save()

        # 해당 회원을 그냥 탈퇴시킴
        user = get_object_or_404(User, username = data['user'])
        user.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE'])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'GET':
        serializer = BoardSerializer(board)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        # comments = Comment.objects.all()
        comments = get_list_or_404(Comment)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, board_pk):
    # article = Article.objects.get(pk=article_pk)
    board = get_object_or_404(Board, pk=board_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
