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
movie_id_list = [330457,574302,299534,476669,157336,293413,110415,68721,68718,242,220176,372058,568160,11658,18438,773867,619803,518068,282631,396535,496243,200085,437103,567646,385128,158445,72190,209764,107235,79224,51608,47748]
extra_settings = [
        {"skill_type": "nuff", "skill_range": 20, "skill_comment": "얼어 붙어라!", "attack_damage" : 0, "hp": 0, "description":"모든 카드에게 데미지를 20씩 줍니다."},
        {"skill_type": "draw", "skill_range": 2, "skill_comment": "나는 밑에서 한장 너는 위에서 한장", "attack_damage": 0, "hp":0, "description": "카드를 두 장 드로우 합니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "나는 필연적 존재이다!", "attack_damage": 0, "hp":0, "description":"자신과 상대방 둘 중 한명의 체력이 반으로 줄어듭니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "Manners makes man", "attack_damage": 0, "hp":0, 'description' : "콘솔창이 존대말로 바뀝니다."},
        {"skill_type": "heal", "skill_range": 10, "skill_comment": "We will find a way. we always have.", "attack_damage": 0, "hp":0, 'description' : "모든 유닛의 체력이 +10 회복됩니다."},
        {"skill_type": "nuff", "skill_range": -10, "skill_comment": "대중들은 개,돼지 입니다. 적당히 짖어대다 알아서 조용해질 겁니다.", "attack_damage": 30, "hp": 40, 'description' : "모든 유닛의 체력이 -10이 됩니다. "},
        {"skill_type": "heal", "skill_range": +30, "skill_comment": "프로틴-바", "attack_damage": 0, "hp": 0, 'description' : "캐릭터의 체력이 +30 증가합니다."},
        {"skill_type": "buff", "skill_range": +10, "skill_comment": "I am Iron man", "attack_damage": 0, "hp": 0, 'description' : "모든 하수인의 공격력이 + 10이 됩니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "백엔드의 신", "attack_damage": 40, "hp": 40, 'description' : "쟝-고"},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "친구는 가까이 두고, 적은 더 가까이 두어야 한다.", "attack_damage": 0, "hp": 0, 'description' : "적이 한턴 공격을 쉽니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "내가 왕이 될 상인가", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 공격력 60 or 공격력 1이 됩니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "키미노 나마에와", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 이번턴 적 챔피언과 공격력이 바뀝니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "하지만, 내가 돌아가면, 다시 날씨가..!", "attack_damage": 0, "hp": 0, 'description' : "필드가 바뀝니다. 상대방의 다음턴 공격력이 -5만큼 감소합니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "넌 내 꿈이구 어머니 희망이야. 어서 가.", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 해당 하수인이 손으로 돌아갑니다. 필드 하수인들의 체력이 +10이 됩니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "아무도 없으면 외롭지 않으니까요.", "attack_damage": 0, "hp": 0, 'description' : "필드에 아무것도 없다면 50/50짜리 김씨를 소환합니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "우린 노빠꾸다!", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 하수인의 공격력이 40 체력이 1이 됩니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "누가 50이야?", "attack_damage": 20, "hp": 100, 'description' : "그냥 강합니다."},
        {"skill_type": "heal", "skill_range": 20, "skill_comment": "지나간 일에 새로운 눈물을 낭비하지 말자", "attack_damage": 0, "hp": 0, 'description' : "모든 하수인이 +20 회복됩니다."},
        {"skill_type": "buff", "skill_range": 10, "skill_comment": "신에게는 아직 12척의 배가 남아있습니다", "attack_damage": 0, "hp": 0, 'description' : "모든 하수인의 공격력이 +10 증가합니다."},
        {"skill_type": "draw", "skill_range": 3, "skill_comment": "이 사람들 빨리 내보내야돼. 안 그러면 우리까지 위험해져", "attack_damage": 0, "hp": 0, 'description' : "카드를 3장 뽑습니다."},
        {"skill_type": "draw", "skill_range": 3, "skill_comment": "착해서 돈이 많은 게 아니라 돈이 많으니까 착한 거야", "attack_damage": 0, "hp": 0, 'description' : "카드를 3장 뽑습니다."},
        {"skill_type": "nuff", "skill_range": 10, "skill_comment": "이런 고병원성 바이러스에 늑장 대응하다가 구제역 사태처럼 전국으로 퍼지기라도 한다면 큰일입니다", "attack_damage": 30, "hp": 60, 'description' : "다른 모든 하수인의 체력이 -10 감소합니다."},
        {"skill_type": "draw", "skill_range": 3, "skill_comment": "경찰이 고문해서 대학생이 죽었는데, 보도지침이 대수야?", "attack_damage": 0, "hp": 0, 'description' : "카드를 3장 뽑습니다."},
        {"skill_type": "heal", "skill_range": 40, "skill_comment": "왕갈비통닭 한마리요~", "attack_damage": 0, "hp": 0, 'description' : "하수인 또는 캐릭터를 선택합니다. 체력이 +40 증가합니다."},
        {"skill_type": "buff", "skill_range": 40, "skill_comment": "작별인사는 하고 가야지", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 이번턴 하수인의 공격력이 +40 증가합니다."},
        {"skill_type": "heal", "skill_range": 40, "skill_comment": "아빠 딸로 태어나줘서 고맙습니다.", "attack_damage": 0, "hp": 0, 'description' : "내 캐릭터의 체력이 +40 증가합니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "사람은 어떤 일이 터진 후에야 후회해. 이건 인간이 멍하거나 나약해서가 아니라. 본능 때문이야", "attack_damage": 40, "hp": 60, 'description' : "필드의 모든 하수인을 파괴합니다."},
        {"skill_type": "draw", "skill_range": 3, "skill_comment": "나 지금 이거 일생일대 기횐 거 같애", "attack_damage": 0, "hp": 0, 'description' : "덱에서 카드를 3장 뽑습니다."},
        {"skill_type": "heal", "skill_range": 10, "skill_comment": "비벼~ 막비벼~", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 해당 하수인의 양 옆의 체력이 +10 증가합니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "두려움은 직시하면 그 뿐. 바람은 계산하는 것이 아니라 극복하는 것이다.", "attack_damage": 0, "hp": 0, 'description' : "보스의 체력이 20 이하라면 즉사합니다. 아니라면 -10의 데미지를 줍니다."},
        {"skill_type": "buff", "skill_range": 40, "skill_comment": "내일을 사는 놈은 오늘만 사는 놈을 못이긴다.", "attack_damage": 0, "hp": 0, 'description' : "하수인을 선택합니다. 해당 하수인의 공격력이 +40 증가합니다. 이번턴에 사망합니다."},
        {"skill_type": "others", "skill_range": 0, "skill_comment": "음 머~", "attack_damage": 0, "hp": 60, 'description' : "이 소를 죽이지 말아주세요..."},
]
for i in range(len(movie_id_list)):
        res = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id_list[i]}?api_key={tmdb_api_key}&language=ko')
        data = res.json()
        unique_list.append({"id": movie_id_list[i], "name": data['title'], "poster_path": data['poster_path'],"attack_damage": extra_settings[i]['attack_damage'],"hp" : extra_settings[i]['hp'],"skill_type": extra_settings[i]['skill_type'],"skill_range": extra_settings[i]['skill_range'], "skill_comment": extra_settings[i]['skill_comment'], "skill_description": extra_settings[i]['description']})

# print(unique_list)