from django.urls import path
from . import views


urlpatterns = [
    path('', views.scoreboard_list),
    path('<int:board_pk>/', views.board_detail),
    path('comments/', views.comment_list),
    # path('comments/<int:comment_pk>/', views.comment_detail),
    path('<int:board_pk>/comments/', views.comment_create),
]
