from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CardSerializer,NormalCardSerializer,UniqueCardSerializer,BossCardSerializer, SkillSerializer
from .models import Card,NormalCard,UniqueCard,BossCard,Skill

import random
import requests
import json

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def cards_list(request): # 전체 카드를 보여준다.
    print(1)
    card = get_list_or_404(Card)
    serializer = CardSerializer(card, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def normalcard_list(request): # 평범한 카드 리스트를 확인한다.
    if request.method == 'GET':
        normal_card = get_list_or_404(NormalCard)
        serializer = NormalCardSerializer(normal_card, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 여기서 기존 DB 전체 삭제
        data = get_list_or_404(Card)
        for i in data:
            Card.delete(i)
        # 해리포터 id 리스트
        harry_list = [671,672,673,674,675,767,12445]
        for i in range(1,11): # Page를 가져온다. => 20개마다 5개씩으로 산정
            res = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=6c79aec26c8ca6dcd33960ef33a7008a&page={i}&language=ko')
            database = res.json()['results'] # dic형태로 나타난다. => 데이터 들고옴!
            for data in database: # 상위 200개 들고옴
                if data["id"] not in harry_list:
                    card = Card(movie_id=data['id'],movie_type='normal')
                    card.save()

            normal_card_database = random.sample(database, 5) # 20개 중에 5 개 뽑으면 됨
            for data in normal_card_database: 
                if data["id"] not in harry_list:
                    normal_card = NormalCard(card=card, name=data['title'], poster_path = str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"),attack_damage = int(data["vote_average"]*3), hp = int(data['popularity']//10))
                normal_card.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def bosscard_list(request): # 보스 카드를 더한다.
    if request.method == 'GET':
        bosscard = get_list_or_404(BossCard)
        serializer = BossCardSerializer(bosscard, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        boss_info = [{"id":671,"name": '스네이프', "poster_path":'', "AD": 18, "HP": 199, "skill_type":["heal"], "skill_range":[100], "skill_comment":["엄마의 눈을 꼭 닮았구나"]},
        {"id":672, "name": '헤르미온느', "poster_path":'', "AD": 28, "HP": 237, "skill_type":["buff","deal"], "skill_range":[100,-40], "skill_comment":["규칙을 어기는 일, 흥분된다!","윙가르디움 레비오우사"]},
        {"id":673, "name": '도비', "poster_path":'', "AD": 3, "HP": 500, "skill_type":['heal','alldeal'], "skill_range": [50,12], "skill_comment":["도비는 자유예요","도비는 자유로운 집요정이예요"]},
        {"id":674,"name": '볼드모트', "poster_path":'', "AD": 50, "HP": 302, "skill_type":['deal','attacknuff','healnuff'], "skill_range":[10000,-50,-50], "skill_comment":["Avracadabra","I can touch you now","죽음을 먹는 자"]},
        {"id":675,"name": '해리포터', "poster_path":'', "AD": 10, "HP": 303, "skill_type":['others','others','others'], "skill_range":[0,0,0], "skill_comment":['입 닥 쳐 말포이','Expecto Patronum', '아씨오 론 위즐리']},
        {"id":767,"name": '헤드위그', "poster_path":'', "AD": 8, "HP": 100, "skill_type":['alldeal','heal'], "skill_range":[50,-100], "skill_comment":["부엉부엉","엉부엉부"]},
        {"id":12445,"name": '마법의 모자', "poster_path":'', "AD": 0, "HP": 1000, "skill_type":["others","others"], "skill_range":[0,0], "skill_comment":["구리퓐도르!","임페리오"]}]
        harry_list = [671,672,673,674,675,767,12445]
        for i in range(7):
            if boss_info[i]['id'] not in harry_list:
                continue
            # Card Table에 추가
            card = Card(movie_id=boss_info[i]["id"],movie_type='boss')
            card.save()
            # BossCard Table에 추가
            bosscard = BossCard(card = card, name=boss_info[i]['name'], poster_path = boss_info[i]['poster_path'], attack_damage = boss_info[i]["AD"], hp = boss_info[i]["HP"])
            bosscard.save()
            # SkillCard Table에 추가
            for j in range(len(boss_info[i]['skill_type'])):
                skillcard = Skill(card=card, skill_type=boss_info[i]['skill_type'][j], skill_range=boss_info[i]['skill_range'][j], skill_comment=boss_info[i]['skill_comment'][j])
                skillcard.save()
        return Response(status=status.HTTP_201_CREATED)

#str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}")
# @api_view(['GET','POST'])
# # @permission_classes([IsAuthenticated])
# def bosscard_plus(request): # 보스 카드를 더한다.
#     if request.method == 'GET':
#         bosscard = get_list_or_404(BossCard)
#         serializer = BossCardsSerializer(bosscard, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         boss_list = [i for i in range(671,676)] + [767,12445]
#         # GET
#         for i in boss_list:
#             res = requests.get(f'https://api.themoviedb.org/3/movie/{i}?api_key=6c79aec26c8ca6dcd33960ef33a7008a&page=1&language=ko')
#             data = res.json()
#             card = BossCards(name=data['title'], poster_path = str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"), attack_damage =int(data["vote_average"]*10), hp = int(data['popularity']//10))
#             # result.append({"name":data['title'], 'poster_path': str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"), "AD": int(data["vote_average"]*10), "HP": int(data['popularity']//10)})
#             card.save()
#         return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def skill_list(request):
    bosscard = get_list_or_404(Skill)
    serializer = SkillSerializer(bosscard, many=True)
    return Response(serializer.data)
