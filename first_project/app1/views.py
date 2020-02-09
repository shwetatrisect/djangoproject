from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index Page")
    
def music(request):
    return HttpResponse("Music Page")

def videos(request):
    return HttpResponse("Videos Page")

def music_mp3(request):
    return HttpResponse("Mp3 page")
