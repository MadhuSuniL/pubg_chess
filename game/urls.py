
from django.contrib import admin
from django.urls import path
from game.views import *
urlpatterns = [
    path('', game),
    path('get_poses/', get_backend_pos),
    path('get_opnt_poses/', get_opnt_backend_pos),
    path('make_none/', make_none_view),
    path('set_poses/', set_backend_pos),
    path('inc_health/', inc_health),
    path('dec_health/', dec_health),
    path('get_health/', get_health),
    path('blinks/', blinks_view),
    path('kill/', kill),
]
