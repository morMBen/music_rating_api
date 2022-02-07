from django.shortcuts import render
from rest_framework import viewsets
from .models import Song, Rating
from .serializers import SongSerializer, RatingSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

