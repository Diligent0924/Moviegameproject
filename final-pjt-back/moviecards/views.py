from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import BossCardsSerializer
from .models import BossCards

# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated]) # 관리자 권한으로 변경 필요!
def boss(request):
    cards = get_list_or_404(BossCards)
    print(cards)
    return

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def cards_list(request):
    return
    # articles = get_list_or_404(Article)
    # serializer = ArticleListSerializer(articles, many=True)
    # return Response(serializer.data)

# Card Plus
import requests
import json
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def bosscard_list(request): # 그냥 보스를 더할 때 쓰는 곳
    if request.method == 'GET':
        cards = get_list_or_404(BossCards)
        serializer = BossCardsSerializer(cards, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        boss_list = [i for i in range(671,676)] + [767,12445]
        # GET
        for i in boss_list:
            res = requests.get(f'https://api.themoviedb.org/3/movie/{i}?api_key=6c79aec26c8ca6dcd33960ef33a7008a&page=1&language=ko')
            data = res.json()
            card = BossCards(name=data['title'], poster_path = str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"), attack_damage =int(data["vote_average"]*10), hp = int(data['popularity']//10))
            # result.append({"name":data['title'], 'poster_path': str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"), "AD": int(data["vote_average"]*10), "HP": int(data['popularity']//10)})
            card.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','DELETE'])
def bosscard_detail(request, bosscard_pk):
    bosscard = get_object_or_404(BossCards, pk=bosscard_pk)
    if request.method == 'GET':
        serializer = BossCardsSerializer(bosscard)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        BossCards.delete(bosscard)
        return Response(status=status.HTTP_204_NO_CONTENT)
