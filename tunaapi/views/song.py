"""View module for handling requests about songs"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from tunaapi.models import Song



class SongView(ViewSet):
    """Tuna api song view"""
    
    def retrieve(self, request, pk):
      """Handle GET requests for single song
      
      Returns:
        Response -- JSON serialized song
        """
      try:  
          song = Song.objects.get(pk=pk)
          serializer = SongSerializer(song)
          return Response(serializer.data)
      except Song.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
    
    def list(self, request):
      """Handle GET requests to get all songs
      
      Returns:
          Response -- JSON serialized list of songs
      """
      
      songs = Song.objects.all()
      
      # filter to query songs by artist_id
      artist = request.query_params.get('artist_id', None)
      if artist is not None:
          songs = songs.filter(artist_id_id=artist)
          
      serializer = SongSerializer(songs, many=True)
      return Response(serializer.data)
    

class SongSerializer(serializers.ModelSerializer):
  """JSON serializer for songs"""
  
  class Meta:
      model = Song
      fields = ('id', 'title', 'artist_id', 'album', 'length')
      depth = 1
