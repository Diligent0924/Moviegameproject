from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_count), # 해당 영화가 몇번이나 쓰였는지를 확인해서 TDMB에서 받아서 던져주는역할
    path('<int:movie_pk>/', views.movie_detail), # 개별적인 정보를 보여주는 역할
]
