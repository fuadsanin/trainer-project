from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def new_team(request):
    return render(request,'new_team.html')
def new_team1(request):
    return render(request,'new_team1.html')

 

