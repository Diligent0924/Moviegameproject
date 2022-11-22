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
    for movie in movie_list:
        res = requests.get(f'https://api.themoviedb.org/3/movie/{movie.movie_id}?api_key={tmdb_api_key}&language=ko')
        print(type(res))
        data = res.json()
        needs = ["title",'vote_average','vote_count',"genres","poster_path","release_date","runtime","tagline"]
        dic = {}
        for i in needs:
            dic[i] = data[i]
        a = json.dumps(dic, ensure_ascii=False)
        algorithm_movie_list.append(a)
    return Response(algorithm_movie_list)

def movie_detail(request):
    return Response()