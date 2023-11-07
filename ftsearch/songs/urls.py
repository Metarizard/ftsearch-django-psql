from django.urls import path

from songs.views import SongListView



urlpatterns = [
    path("songs/", SongListView.as_view(), name="songs"),
]
