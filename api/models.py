from django.db import models
from django.contrib.auth.models import User  # import  the connected user
from django.core.validators import MaxValueValidator, MinValueValidator


class Song(models.Model):
    title = models.CharField(max_length=32)
    artist = models.CharField(max_length=32)
    type = models.TextField(max_length=360)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(song=self)
        return len(ratings)

    def avg_ratings(self):
        sum_of_ratings = 0
        ratings = Rating.objects.filter(song=self)
        for rating in ratings:
            sum_of_ratings += rating.stars

        if len(ratings) > 0:
            return sum_of_ratings / len(ratings)
        else:
            return 0


class Rating(models.Model):
    # on_delete=models.CASCADE saying if we delete the song we delete the rating
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'song'),)
        index_together = (('user', 'song'),)
