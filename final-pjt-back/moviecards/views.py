from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CardSerializer,NormalCardSerializer,UniqueCardSerializer,BossCardSerializer, UniqueSkillSerializer,BossSkillSerializer,normaldetailSerializer,UniquedetailSerializer,BossdetailSerializer,plusSerializer
from .models import Card,NormalCard,UniqueCard,BossCard,UniqueSkill,BossSkill

import random
import requests
import json
from .apikey import tmdb_api_key
from .data import boss_info, unique_list

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def cards_list(request): # 전체 카드를 보여준다.
    card = Card.objects.raw("SELECT * from moviecards_card")
    serializer = CardSerializer(card, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def normalcard_list(request): # 평범한 카드 리스트를 확인한다.
    if request.method == 'GET':
        normal_card = NormalCard.objects.raw("SELECT * from moviecards_normalcard")
        print(normal_card)
        serializer = NormalCardSerializer(normal_card, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 여기서 기존 DB 전체 삭제
        data = Card.objects.raw('select * from moviecards_card where movietype != "boss"')
        for i in data:
            Card.delete(i)
        # 해리포터 id 리스트
        harry_list = [671,672,673,674,675,767,12445]
        for i in range(1,11): # Page를 가져온다. => 20개마다 5개씩으로 산정
            res = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key={tmdb_api_key}&page={i}&language=ko')
            database = res.json()['results'] # dic형태로 나타난다. => 데이터 들고옴!
            for data in database: # 상위 20개씩 들고온다.
                if data["id"] not in harry_list:
                    card = Card(movieid=data['id'],movietype='normal')
                    card.save()
                    normal_card = NormalCard(card=card, name=data['title'], posterpath = str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"),attackdamage = int(data["vote_average"]*3), hp = int(data['popularity']**(1/2)))
                    normal_card.save()
        return Response(status=status.HTTP_201_CREATED)

# 특수 카드를 더하는 공간
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def uniquecard_list(request):
    if request.method == 'GET':
        uniquecard = BossCard.objects.raw("select * from moviecards_uniquecard")
        serializer = UniqueCardSerializer(uniquecard, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        for unique_card in unique_list:
            card = Card(movieid=unique_card['id'],movietype='unique')
            card.save()

            uniquecard = UniqueCard(card = card, name=unique_card['name'], posterpath = unique_card['poster_path'], attackdamage = unique_card["attack_damage"], hp = unique_card["hp"])
            uniquecard.save()

            skillcard = UniqueSkill(card=uniquecard, skilltype=unique_card['skill_type'], skillrange=unique_card['skill_range'], skillcomment=unique_card['skill_comment'])
            skillcard.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def bosscard_list(request): # 보스 카드를 더한다.
    if request.method == 'GET':
        bosscard = BossCard.objects.raw("select * from moviecards_bosscard")
        serializer = BossCardSerializer(bosscard, many=True)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 중복방지 필요
        bosscard = BossCard.objects.raw('select * from moviecards_bosscard')
        if len(bosscard) >= 7: # BossCard를 보내줘야지!
            serializer = BossCardSerializer(bosscard, many=True)
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        for i in range(7): 
            card = Card(movieid=boss_info[i]["id"],movietype='boss')
            card.save()
            # BossCard Table에 추가
            bosscard = BossCard(card = card, name=boss_info[i]['name'], posterpath = boss_info[i]['poster_path'], attackdamage = boss_info[i]["AD"], hp = boss_info[i]["HP"])
            bosscard.save()
            # SkillCard Table에 추가
            for j in range(len(boss_info[i]['skill_type'])):
                skillcard = BossSkill(card=bosscard, skilltype=boss_info[i]['skill_type'][j], skillrange=boss_info[i]['skill_range'][j], skillcomment=boss_info[i]['skill_comment'][j])
                skillcard.save()
        return Response(status=status.HTTP_201_CREATED)

# 스킬 카드들의 집합소
@api_view(['GET'])
def skill_list(request):
    # bosscard = get_list_or_404(Skill)
    # serializer = SkillSerializer(bosscard, many=True)
    return Response()

# 카드들을 확인할 수 있는 곳
@api_view(['GET']) 
def card_detail(request, card_pk):
    card = Card.objects.raw(f'select * from moviecards_card where movieid={card_pk}') # 리스트형태로 준다.
    print(card[0].movietype)
    # movietype이 normal, unique, boss 중 어떤 것이냐에 따라서 serializer를 다르게 보내준다.
    if card[0].movietype == 'normal':
        serializer = normaldetailSerializer(card[0])
        return Response(serializer.data)
    elif card[0].movietype == 'unique':
        serializer = UniquedetailSerializer(card[0])
        return Response(serializer.data)
    else:
        serializer = BossdetailSerializer(card[0])
        return Response(serializer.data)

@api_view(['GET']) # POST로 변경 필요
def plus(request):
    # Normal Card하고 Unique 카드 비율을 어떻게 산정할 것인지에 대한 논의가 필요함...
    card = Card.objects.raw('select * from moviecards_card where movietype != "boss" order by rand() limit 3')
    play_card = [] # 플레이할 카드!
    for data in card:
        selected = Card.objects.raw(f'select * from (select * from moviecards_card where movieid = {data.movieid}) as s1 join moviecards_{data.movietype}card as s2 on s1.movieid = s2.card_id left join moviecards_uniqueskill as s3 on s1.movieid = s3.card_id')
        play_card.append(selected[0])
    
    serializer = plusSerializer(play_card, many=True)
    return Response(serializer.data) 


#str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}")