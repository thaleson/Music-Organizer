# tests.py

from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Artist, Song, Playlist

class MusicAPITests(TestCase):
    """
    Conjunto de testes para as views da API relacionadas aos modelos Artist, Song e Playlist.
    """
    def setUp(self):
        """
        Configuração inicial para os testes.
        """
        self.artist = Artist.objects.create(name='Test Artist')
        self.song = Song.objects.create(title='Test Song', artist=self.artist)
        self.playlist = Playlist.objects.create(name='Test Playlist')
        self.playlist.songs.add(self.song)
        self.client = APIClient()

    def test_artist_list_create(self):
        """
        Testa a listagem e criação de artistas.
        """
        url = reverse('artist-list-create')

        # Verifica se a listagem de artistas retorna status HTTP 200 OK.
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Testa a criação de um novo artista.
        data = {'name': 'New Artist'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 2)

    def test_song_list_create(self):
        """
        Testa a listagem e criação de músicas.
        """
        url = reverse('song-list-create')

        # Verifica se a listagem de músicas retorna status HTTP 200 OK.
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Testa a criação de uma nova música.
        data = {'title': 'New Song', 'artist': self.artist.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Song.objects.count(), 2)

    def test_playlist_list_create(self):
        """
        Testa a listagem e criação de playlists.
        """
        url = reverse('playlist-list-create')

        # Verifica se a listagem de playlists retorna status HTTP 200 OK.
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Testa a criação de uma nova playlist.
        data = {'name': 'New Playlist', 'songs': [self.song.id]}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Playlist.objects.count(), 2)
    