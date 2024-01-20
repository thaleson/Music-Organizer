from django.urls import path
from music_app.views import ArtistListCreateView, SongListCreateView, PlaylistListCreateView

urlpatterns = [
    path('artists/', ArtistListCreateView.as_view(), name='artist-list-create'),
    path('songs/', SongListCreateView.as_view(), name='song-list-create'),
    path('playlists/', PlaylistListCreateView.as_view(),
         name='playlist-list-create'),
]
