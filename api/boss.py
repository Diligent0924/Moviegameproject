import requests
import json

boss_list = [i for i in range(671,676)] + [767,12445]
result = []
# GET
for i in boss_list:
    res = requests.get(f'https://api.themoviedb.org/3/movie/{i}?api_key=6c79aec26c8ca6dcd33960ef33a7008a&page=1&language=ko')
    data = res.json()    
    result.append({"name":data['title'], 'poster_path': str(f"https://image.tmdb.org/t/p/w500{data['poster_path']}"), "AD": int(data["vote_average"]*10), "HP": int(data['popularity']//10)})

print(result)