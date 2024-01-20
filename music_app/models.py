from django.db import models

class Artist(models.Model):
    """
    Modelo para representar um artista de música.

    Campos:
        - name (CharField): O nome do artista (com até 100 caracteres).
    """
    name = models.CharField(max_length=100)

class Song(models.Model):
    """
    Modelo para representar uma música.

    Campos:
        - title (CharField): O título da música (com até 100 caracteres).
        - artist (ForeignKey): Chave estrangeira para associar a música a um artista.
    """
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Playlist(models.Model):
    """
    Modelo para representar uma playlist de músicas.

    Campos:
        - name (CharField): O nome da playlist (com até 100 caracteres).
        - songs (ManyToManyField): Relacionamento muitos para muitos com músicas.
    """
    name = models.CharField(max_length=100)
    songs = models.ManyToManyField(Song)
