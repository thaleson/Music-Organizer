# views.py

from rest_framework import generics
from .models import Artist, Song, Playlist
from .serializers import ArtistSerializer, SongSerializer, PlaylistSerializer

class ArtistListCreateView(generics.ListCreateAPIView):
    """
    View para listar e criar artistas.

    Métodos HTTP permitidos:
        - GET: Obtém a lista de artistas.
        - POST: Cria um novo artista.

    Parâmetros de consulta (GET):
        Nenhum.

    Corpo da solicitação (POST):
        Exemplo:
        {
            "name": "Novo Artista"
        }

    Respostas:
        - Status 200 OK (GET): Retorna a lista de artistas existentes.
        - Status 201 Created (POST): Artista criado com sucesso.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class SongListCreateView(generics.ListCreateAPIView):
    """
    View para listar e criar músicas.

    Métodos HTTP permitidos:
        - GET: Obtém a lista de músicas.
        - POST: Cria uma nova música.

    Parâmetros de consulta (GET):
        Nenhum.

    Corpo da solicitação (POST):
        Exemplo:
        {
            "title": "Nova Música",
            "artist": 1  # Substitua 1 pelo ID do artista existente
        }

    Respostas:
        - Status 200 OK (GET): Retorna a lista de músicas existentes.
        - Status 201 Created (POST): Música criada com sucesso.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class PlaylistListCreateView(generics.ListCreateAPIView):
    """
    View para listar e criar playlists.

    Métodos HTTP permitidos:
        - GET: Obtém a lista de playlists.
        - POST: Cria uma nova playlist.

    Parâmetros de consulta (GET):
        Nenhum.

    Corpo da solicitação (POST):
        Exemplo:
        {
            "name": "Nova Playlist",
            "songs": [1, 2]  # Substitua 1 e 2 pelos IDs das músicas existentes
        }

    Respostas:
        - Status 200 OK (GET): Retorna a lista de playlists existentes.
        - Status 201 Created (POST): Playlist criada com sucesso.
    """
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
