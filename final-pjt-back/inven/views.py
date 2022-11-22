from rest_framework.response import Response
from rest_framework.decorators import api_view
# Authentication Decorators
# from rest_framework.decorators import authentication_classes

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieCountSerializer
from .models import Moviecount
import requests
from moviecards.apikey import tmdb_api_key
import json
# Create your views here.
@api_view(['GET', 'POST'])
def movie_count(request):
    movie_list = Moviecount.objects.raw("select movie_id, count(*) as count from inven_moviecount group by movie_id order by count") # group by로 가져옴.
    algorithm_movie_list = []
    recommend_range = min(100,len(movie_list)) # 100개까지만 보여준다.
    for i in range(recommend_range):
        res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_list[i].movie_id}?api_key={tmdb_api_key}&language=ko')
        data = res.json()
        needs = ["id","title",'vote_average','vote_count',"genres","poster_path","release_date","runtime","tagline"]
        dic = {}
        for j in needs:
            dic[j] = data[j]
        # a = json.dumps(dic, ensure_ascii=False)
        algorithm_movie_list.append(dic)
        # algorithm_movie_list.append(data)
        # return Response(data)
    return Response(algorithm_movie_list)

@api_view(['GET', 'POST'])
def movie_detail(request, movie_pk):
    # "backdrop_path", "overview", "popularity"
    list_a = []
    res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_pk}?api_key={tmdb_api_key}&language=ko')
    data = res.json()
    dic = {}
    needs = ["id","title",'vote_average','vote_count',"genres","poster_path","release_date","runtime","tagline","backdrop_path", "overview", "popularity"]
    for i in needs:
        dic[i] = data[i]
    list_a.append(dic)
    return Response(list_a)