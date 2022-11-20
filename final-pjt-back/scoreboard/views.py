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



@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def scoreboard_list(request):
    if request.method == 'GET': # 전체데이터확인
        articles = Board.objects.raw('select * from scoreboard_board')
        serializer = BoardListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        board = Board(stage=data['stage'],user=data['user'], title=data['title'], content=data['content'])
        board.save()
        # 해당 카드를 세부정보에 표현하는 방식..!
        for movie_id in data["movie_id"]:
            card = Card.objects.raw(f'select * from moviecards_card where movieid = {movie_id}')
            result = Card.objects.raw(f'select * from (select * from moviecards_card where movieid = {card[0].movieid} )as s1 join moviecards_{card[0].movietype}card as s2 on s1.movieid = s2.card_id left join moviecards_skill as s3 on s1.movieid = s3.card_id')
            if card[0].movietype == 'normal':
                moviecard = MovieCard(board=board, movie_id=result[0].movieid, movietype=result[0].movietype, name = result[0].name, posterpath=result[0].posterpath, attackdamage=result[0].attackdamage, hp=result[0].hp)            
            else:
                moviecard = MovieCard(board=board, movie_id=result[0].movieid, movietype=result[0].movietype, name = result[0].name, posterpath=result[0].posterpath, attackdamage=result[0].attackdamage, hp=result[0].hp, skillcomment=result[0].skillcomment)            
            print(result[0].movietype)
            moviecard.save() 
        return Response(status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE'])
def board_detail(request, board_pk):
    # card = Card.objects.raw('select * from moviecards_card where ')
    # article = Article.objects.raw('select * from articles_article as s1 join moviecards_card as s2 on s1.movie_id = s2.movieid join moviecards') # 카드가 30개가 들어있기 때문에 filter로 거쳐야한다.

    board = get_object_or_404(Board, pk=board_pk)
    print(board)
    if request.method == 'GET':
        serializer = BoardSerializer(board)
        print(serializer.data)
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


# @api_view(['GET', 'DELETE', 'PUT'])
# # @permission_classes([IsAuthenticated])
# def comment_detail(request, comment_pk):
#     # comment = Comment.objects.get(pk=comment_pk)
#     comment = get_object_or_404(Comment, pk=comment_pk)

#     if request.method == 'GET':
#         serializer = CommentSerializer(comment)
#         return Response(serializer.data)

#     elif request.method == 'DELETE':
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'PUT':
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)

    


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def comment_create(request, board_pk):
    # article = Article.objects.get(pk=article_pk)
    board = get_object_or_404(Board, pk=board_pk)
    print(board)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(board=board)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
