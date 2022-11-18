from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CardSerializer,NormalCardSerializer,UniqueCardSerializer,BossCardSerializer, SkillSerializer,normaldetailSerializer
from .models import Card,NormalCard,UniqueCard,BossCard,Skill

import random
import requests
import json

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
            res = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=6c79aec26c8ca6dcd33960ef33a7008a&page={i}&language=ko')
            database = res.json()['results'] # dic형태로 나타난다. => 데이터 들고옴!
            for data in database: # 상위 20개씩 들고온다.
                if data["id"] not in harry_list:
                    card = Card(movieid=data['id'],movietype='normal')
                    card.save()
                    normal_card = NormalCard(card=card, name=data['title'], posterpath = str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"),attackdamage = int(data["vote_average"]*3), hp = int(data['popularity']//10))
                    normal_card.save()
                    

            # normal_card_database = random.sample(database, 5) # 20개 중에 5 개 뽑으면 됨
            # for data in normal_card_database: 
            #     if data["id"] not in harry_list:
            #         card = get_object_or_404(Card, movieid=data['id'])
        return Response(status=status.HTTP_201_CREATED)

# 특수 카드를 더하는 공간
@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def uniquecard_list(request):
    if request.method == 'GET':
        bosscard = BossCard.objects.raw("select * from moviecards_uniquecard")
        serializer = UniqueCardSerializer(bosscard, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # for i in range(7): 
        #     if boss_info[i]['id'] not in harry_list:
        #         continue
        #     # Card Table에 추가
        #     card = Card(movie_id=boss_info[i]["id"],movie_type='boss')
        #     card.save()
        #     # BossCard Table에 추가
        #     bosscard = BossCard(card = card, name=boss_info[i]['name'], poster_path = boss_info[i]['poster_path'], attack_damage = boss_info[i]["AD"], hp = boss_info[i]["HP"])
        #     bosscard.save()
        #     # SkillCard Table에 추가
        #     for j in range(len(boss_info[i]['skill_type'])):
        #         skillcard = Skill(card=card, skill_type=boss_info[i]['skill_type'][j], skill_range=boss_info[i]['skill_range'][j], skill_comment=boss_info[i]['skill_comment'][j])
        #         skillcard.save()
        return Response(status=status.HTTP_201_CREATED)

@api_view(['GET','POST'])
# @permission_classes([IsAuthenticated])
def bosscard_list(request): # 보스 카드를 더한다.
    if request.method == 'GET':
        bosscard = BossCard.objects.raw("select * from moviecards_bosscard")
        serializer = BossCardSerializer(bosscard, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # 중복방지 필요 => 
        boss_info = [{"id":671,"name": '스네이프', "poster_path":'', "AD": 18, "HP": 199, "skill_type":["heal"], "skill_range":[100], "skill_comment":["엄마의 눈을 꼭 닮았구나"]},
        {"id":672, "name": '헤르미온느', "poster_path":'', "AD": 28, "HP": 237, "skill_type":["buff","deal"], "skill_range":[100,-40], "skill_comment":["규칙을 어기는 일, 흥분된다!","윙가르디움 레비오우사"]},
        {"id":673, "name": '도비', "poster_path":'', "AD": 3, "HP": 500, "skill_type":['heal','alldeal'], "skill_range": [50,12], "skill_comment":["도비는 자유예요","도비는 자유로운 집요정이예요"]},
        {"id":674,"name": '볼드모트', "poster_path":'', "AD": 50, "HP": 302, "skill_type":['deal','attacknuff','healnuff'], "skill_range":[10000,-50,-50], "skill_comment":["Avracadabra","I can touch you now","죽음을 먹는 자"]},
        {"id":675,"name": '해리포터', "poster_path":'', "AD": 10, "HP": 303, "skill_type":['others','others','others'], "skill_range":[0,0,0], "skill_comment":['입 닥 쳐 말포이','Expecto Patronum', '아씨오 론 위즐리']},
        {"id":767,"name": '헤드위그', "poster_path":'', "AD": 8, "HP": 100, "skill_type":['alldeal','heal'], "skill_range":[50,-100], "skill_comment":["부엉부엉","엉부엉부"]},
        {"id":12445,"name": '마법의 모자', "poster_path":'', "AD": 0, "HP": 1000, "skill_type":["others","others"], "skill_range":[0,0], "skill_comment":["구리퓐도르!","임페리오"]}]

        for i in range(7): 
            card = Card(movieid=boss_info[i]["id"],movietype='boss')
            card.save()
            # BossCard Table에 추가
            bosscard = BossCard(card = card, name=boss_info[i]['name'], posterpath = boss_info[i]['poster_path'], attackdamage = boss_info[i]["AD"], hp = boss_info[i]["HP"])
            bosscard.save()
            # SkillCard Table에 추가
            for j in range(len(boss_info[i]['skill_type'])):
                skillcard = Skill(card=card, skilltype=boss_info[i]['skill_type'][j], skillrange=boss_info[i]['skill_range'][j], skillcomment=boss_info[i]['skill_comment'][j])
                skillcard.save()
        return Response(status=status.HTTP_201_CREATED)

# 스킬 카드들의 집합소
@api_view(['GET'])
def skill_list(request):
    bosscard = get_list_or_404(Skill)
    serializer = SkillSerializer(bosscard, many=True)
    return Response(serializer.data)

# 카드들을 확인할 수 있는 곳
@api_view(['GET'])
def card_detail(request, card_pk):
    card = Card.objects.raw(f'select * from moviecards_card where movieid={card_pk}') # 리스트형태로 준다.
    print(card[0].movietype)
    # Cards와 개별카드 테이블의 경우 1:1이므로 NL을 사용하고 스킬의 경우에는 1:N이기 때문에 left join을 사용해서 구했다.
    card = Card.objects.raw(f'select * from (select * from moviecards_card where movieid = {card_pk} )as s1 join moviecards_{card[0].movietype}card as s2 on s1.movieid = s2.card_id left join moviecards_skill as s3 on s1.movieid = s3.card_id')
    if len(card) == 1: # 만약 card의 개수가 1개라면 해당 카드만 반환 => many=True를 사용할 수 없음
        serializer = normaldetailSerializer(card[0])
        return Response(serializer.data)
    else: # 만약 card의 개수가 2개 이상이라면 해당 카드들을 사용 => many = True를 사용
        serializer = normaldetailSerializer(card, many=True) # 이부분 그냥 일부분만 serialize가 가능할거같은데 나중에 하자!
        return Response(serializer.data)

@api_view(['GET']) # POST로 변경 필요
def plus(request):
    # Normal Card하고 Unique 카드 비율을 어떻게 산정할 것인지에 대한 논의가 필요함...
    card = Card.objects.raw('select * from moviecards_card where movietype != "boss" order by rand() limit 3')
    play_card = [] # 플레이할 카드!
    for data in card:
        selected = Card.objects.raw(f'select * from (select * from moviecards_card where movieid = {data.movieid}) as s1 join moviecards_{data.movietype}card as s2 on s1.movieid = s2.card_id left join moviecards_skill as s3 on s1.movieid = s3.card_id')
        play_card.append(selected[0])
    serializer = normaldetailSerializer(play_card, many=True)
    return Response(serializer.data) 



#str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}")