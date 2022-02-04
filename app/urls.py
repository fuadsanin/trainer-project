from django.urls import path
from app import views

urlpatterns = [ 
    path('', views.index, name="index"),
    path('new_team/',views.new_team, name="new_team"),
    path('new_team1/',views.new_team1, name="new_team1"),    
]
