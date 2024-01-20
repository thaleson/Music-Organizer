# serializers.py

from rest_framework import serializers
from .models import Artist, Song, Playlist


class ArtistSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Artist.

    Atributos:
        id (int): Identificador único do artista.
        name (str): Nome do artista.
        bio (str): Breve biografia ou descrição do artista.
        created_at (datetime): Carimbo de data/hora quando o registro do artista foi criado.
        updated_at (datetime): Carimbo de data/hora quando o registro do artista foi atualizado pela última vez.
    """
    class Meta:
        model = Artist
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Song.

    Atributos:
        id (int): Identificador único da música.
        title (str): Título da música.
        artist (ArtistSerializer): Representação serializada do artista associado.
        album (str): Álbum ao qual a música pertence.
        release_date (date): Data de lançamento da música.
        created_at (datetime): Carimbo de data/hora quando o registro da música foi criado.
        updated_at (datetime): Carimbo de data/hora quando o registro da música foi atualizado pela última vez.
    """
    class Meta:
        model = Song
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    """
    Serializador para o modelo Playlist.

    Atributos:
        id (int): Identificador único da playlist.
        title (str): Título ou nome da playlist.
        songs (SongSerializer(many=True)): Representação serializada das músicas associadas.
        created_at (datetime): Carimbo de data/hora quando o registro da playlist foi criado.
        updated_at (datetime): Carimbo de data/hora quando o registro da playlist foi atualizado pela última vez.
    """
    class Meta:
        model = Playlist
        fields = '__all__'
