import requests
import json

# GET
res = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=6c79aec26c8ca6dcd33960ef33a7008a&page=1&language=ko')
data = res.json()['results'] # dic형태로 나타난다. => 데이터 들고옴!
print(data[0].keys()) # 데이터 들고 온다.

# 세부데이터를 저장하는 방법 
# https://api.themoviedb.org/3/movie/851644?api_key=6c79aec26c8ca6dcd33960ef33a7008a
