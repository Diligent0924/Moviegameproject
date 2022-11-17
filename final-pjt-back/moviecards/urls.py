from django.urls import path
from . import views


urlpatterns = [
    path('', views.cards_list), # 전체 카드 리스트를 전부 보여주자.
    # Card들을 더하는 URL
    path('normalcard_list/', views.normalcard_list),
    # path('uniquecard_list/', views.uniquecard_list),
    path('bosscard_list/', views.bosscard_list),
    path('skill_list/', views.skill_list),
    # path('bosscard_list/<int:bosscard_pk>/', views.bosscard_detail),

    # 추가적인 기능 활동
    # path('firstdeck/', views.firstdeck),
    # path('plus/', views.plus)
]
