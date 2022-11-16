from django.urls import path
from . import views


urlpatterns = [
    path('', views.cards_list),
    path('boss/', views.boss), #보스를 찾아서 주는 url
    # path('firstdeck/', views.firstdeck),
    # path('plus/', views.plus)
    # Card 더하는 URL
    path('bosscard_list/', views.bosscard_list), # 전체 보는곳!
    path('bosscard_list/<int:bosscard_pk>/', views.bosscard_detail),
]
