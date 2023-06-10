from django.db import models
from .artist import Artist


class Song(models.Model):
  
  title = models.CharField(max_length=100)
  artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')
  album = models.CharField(max_length=100)
  length = models.DurationField()
  
  def genres(self):
    return [song_genre.genre_id for song_genre in self.song_genres.all()]
