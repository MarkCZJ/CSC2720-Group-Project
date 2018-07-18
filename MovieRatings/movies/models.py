from django.db import models
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


User = settings.AUTH_USER_MODEL

class Movie(models.Model):

    director_name = models.CharField(max_length=255)
    duration = models.IntegerField()
    actor_2_name = models.CharField(max_length=255)
    gross = models.IntegerField()
    genres = models.CharField(max_length=255)
    actor_1_name = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    num_voted_users = models.CharField(max_length=255)
    actor_3_name = models.CharField(max_length=255)
    movie_imdb_link = models.CharField(max_length=255)
    num_user_for_reviews = models.IntegerField()
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    content_rating = models.CharField(max_length=255)
    budget = models.IntegerField()
    title_year = models.IntegerField()
    imdb_score = models.FloatField()


class UserRatings(models.Model):
    user = models.IntegerField()
    movie_title = models.CharField(max_length=255)
    title_year = models.IntegerField()
    rating = models.IntegerField()

