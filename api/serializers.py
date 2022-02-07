from rest_framework import serializers
from .models import Song, Rating


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'type', 'artist', 'no_of_ratings', 'avg_ratings')


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ('id', 'song', 'user', 'stars')
