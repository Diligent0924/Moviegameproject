import requests
from .apikey import tmdb_api_key
boss_info = [{"id":671,"name": '스네이프', "poster_path":'https://w.namu.la/s/7a41faaffbc04f0cd6d97f170f885108cb2d9a32ae869fd8a66f68efc2f083267fed093f611d6e0527f1e047079562127f6f92890a9f87c934eed75ba577407c0e2bf8dd82f6d5506dc5f79e14bddc931cd49c961b9ea11a1554355508e1cdb0', "AD": 18, "HP": 199, "skill_type":["heal"], "skill_range":[100], "skill_comment":["엄마의 눈을 꼭 닮았구나"]},
        {"id":672, "name": '헤르미온느', "poster_path":'https://w.namu.la/s/ea0c0b04eb136a71ea4356829c9dd629b1867956174232f8dc6c58fabb9af4dac97b7a5852b5c1c8ad882f10d1593fdf0f92714d54ea3cca6cf333d64a78fccf137b9b6278ba0d48116eafc775f9e01369acd8d2cec2034d4e1f414eec3e06417d3a39b42dc98e0a810ffdb12b345434', "AD": 28, "HP": 237, "skill_type":["buff","deal"], "skill_range":[100,-40], "skill_comment":["규칙을 어기는 일, 흥분된다!","윙가르디움 레비오우사"]},
        {"id":673, "name": '도비', "poster_path":'https://w.namu.la/s/f56dd40acd7b237bcb08c1a9b8ef843d352638914f73ce58704549032eef4b974b0e33bd1fec7da814ba8bd47357a7cb9e565ea269aaf0a2ca945ac10b0c41efd25128fb392162692feeab2f0f329b4d716a11fbfbe414b10ad041a46e64be7a9271562bb159dcff4b455963604ea087', "AD": 3, "HP": 500, "skill_type":['heal','alldeal'], "skill_range": [50,12], "skill_comment":["도비는 자유예요","도비는 자유로운 집요정이예요"]},
        {"id":674,"name": '볼드모트', "poster_path":'https://w.namu.la/s/17a52c55a13affa9d31b6dc9b33d77996c2369e05faf975f9ba2ecf3b840c97d1f7bb6ad33422982f3a4fe7398c10cfb82fe57e325eb263c8bd66322856294f6fd52b6c5a1ade274e953ddf9c25644b7dfa4300d4e904707e5e3b02bccdf4b32', "AD": 50, "HP": 302, "skill_type":['deal','attacknuff','healnuff'], "skill_range":[10000,-50,-50], "skill_comment":["Avracadabra","I can touch you now","죽음을 먹는 자"]},
        {"id":675,"name": '해리포터', "poster_path":'https://w.namu.la/s/6bfab95f914ff61216609b6603fc74b249c3da1a6f346df47ff2320f1fe3d9c96ae8744c197e55b2d2049727998129ecb2ace74f73199a9478615de3f3ebb77a5b56270e1d12b190bba7770a09382dd06bda4d808379d5c1e24ff1f02cb848abb0c79dbc1f289197f9c93cff0f3a4e34', "AD": 10, "HP": 303, "skill_type":['others','others','others'], "skill_range":[0,0,0], "skill_comment":['입 닥 쳐 말포이','Expecto Patronum', '아씨오 론 위즐리']},
        {"id":767,"name": '헤드위그', "poster_path":'https://w.namu.la/s/76b0eb94927c846382c8df771c15a4ceab0e946f2cb0ea2ea517e6769ebaf0a199e01435a8582d0be84774a5e5cae2a7b14f5ce680f02c50ba6ad8328b79fee47e3aa7c149ea1d9eb7b5892bbed3626a23ad3de2b750ec156f221b6705adeb35', "AD": 8, "HP": 100, "skill_type":['alldeal','heal'], "skill_range":[50,-100], "skill_comment":["부엉부엉","엉부엉부"]},
        {"id":12445,"name": '마법의 모자', "poster_path":'https://w.namu.la/s/a272c7937937b251dae026df601f345e26eeaf3263a01d401824b000d31ac738f38168da465d49404faf079683ad294320a522bab164d6450fd4e71bce8f090a2dd55bb9d9fd6edb8a1b1633e44b7ac42ce073005eb6480d2715a1ada5381b68799b24312a9cf1c929fc75d5308eecb4', "AD": 0, "HP": 1000, "skill_type":["others","others"], "skill_range":[0,0], "skill_comment":["구리퓐도르!","임페리오"]}]

unique_list = []
movie_id_list = [330457,]
extra_settings = [
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},
        {"skill_type": "hill_nuff", "skill_range": -20, "skill_comment": "얼어 붙어라!"},

]
for i in range(len(movie_id_list)):
        res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id_list[i]}?api_key={tmdb_api_key}&language=ko')
        data = res.json()
        unique_list.append({"id": movie_id_list[i], "name": data['title'], "poster_path": data['poster_path'],"attack_damage": data['vote_average'] * 3,"hp" : data['popularity'],"skill_type": extra_settings[i]['skill_type'],"skill_range": extra_settings[i]['skill_range'], "skill_comment": extra_settings[i]['skill_comment']})
