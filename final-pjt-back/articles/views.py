
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# # Authentication Decorators
# # from rest_framework.decorators import authentication_classes

# # permission Decorators
# from rest_framework.decorators import permission_classes
# from rest_framework.permissions import IsAuthenticated

# from rest_framework import status
# from django.shortcuts import get_object_or_404, get_list_or_404
# from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
# from .models import Article, Comment
# # from ..moviecards.models import Card



# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
# def article_list(request):
#     if request.method == 'GET': # 게시판을 보여줄 때 쓰이는 것
#         # 유저/스테이지/제목/생성날짜만 보이게 하자.
#         articles = Article.objects.raw('select user, stage, title, created_at from articles_article')
#         serializer = ArticleListSerializer(articles, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = ArticleSerializer(data=request.data, many=True) # 데이터 전체를 쏜다.
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET', 'DELETE'])
# def article_detail(request, article_pk):
#     # card = Card.objects.raw('select * from moviecards_card where ')
#     # article = Article.objects.raw('select * from articles_article as s1 join moviecards_card as s2 on s1.movie_id = s2.movieid join moviecards') # 카드가 30개가 들어있기 때문에 filter로 거쳐야한다.
#     article = get_object_or_404(Article, pk=article_pk)
    
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         print(serializer.data)
#         return Response(serializer.data)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET'])
# def comment_list(request):
#     if request.method == 'GET':
#         # comments = Comment.objects.all()
#         comments = get_list_or_404(Comment)
#         serializer = CommentSerializer(comments, many=True)
#         return Response(serializer.data)


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

    


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def comment_create(request, article_pk):
#     # article = Article.objects.get(pk=article_pk)
#     article = get_object_or_404(Article, pk=article_pk)
#     serializer = CommentSerializer(data=request.data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save(article=article)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
