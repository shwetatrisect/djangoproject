from django.conf.urls import url
from app1 import views
urlpatterns = [
    url(r'^music/',views.music,name='music'),
    url(r'^videos/',views.videos,name='videos'),
    url(r'^music_mp3',views.music_mp3,name='music_mp3'),
]
