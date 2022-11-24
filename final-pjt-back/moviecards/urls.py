from django.urls import path
from . import views


urlpatterns = [
    # 전체 Card들을 저장
    path('', views.cards_list),
    # Cards => GET : 카드더미 확인, POST : 카드더미 추가
    path('normalcard_list/', views.normalcard_list),
    path('uniquecard_list/', views.uniquecard_list),
    path('bosscard_list/', views.bosscard_list),
    
    # 개별적인 Card들을 확인
    path('<int:card_pk>/', views.card_detail),

    # 추가적인 기능 활동
    path('plus/', views.plus)
]
