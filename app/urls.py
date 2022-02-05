from django.urls import re_path
from .import views
urlpatterns = [ 
    re_path(r'^$', views.index, name='index'),
    re_path(r'^new_team$', views.new_team, name='new_team'),
    re_path(r'^new_team1$', views.new_team1, name='new_team1'),
    re_path(r'^team_update$', views.team_update, name='team_update'),
]

