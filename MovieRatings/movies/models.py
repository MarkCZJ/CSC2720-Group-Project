from django.db import models

class Movie(models.Model):
    # tconst = models.CharField(max_length=9)
    # primaryTitle = models.CharField(max_length=255)
    # startYear = models.CharField(max_length=255)
    # runtimeMinutes = models.CharField(max_length=255)
    # genres = models.CharField(max_length=32)

    # color = models.CharField(max_length=255)
    director_name = models.CharField(max_length=255)
    # num_critic_for_reviews = models.CharField(max_length=255)
    duration = models.IntegerField()
    # director_facebook_likes = models.CharField(max_length=255)
    # actor_3_facebook_likes = models.CharField(max_length=255)
    actor_2_name = models.CharField(max_length=255)
    # actor_1_facebook_likes = models.CharField(max_length=255)
    gross = models.IntegerField()
    genres = models.CharField(max_length=255)
    actor_1_name = models.CharField(max_length=255)
    movie_title = models.CharField(max_length=255)
    num_voted_users = models.CharField(max_length=255)
    # cast_total_facebook_likes = models.CharField(max_length=255)
    actor_3_name = models.CharField(max_length=255)
    # facenumber_in_poster = models.CharField(max_length=255)
    # plot_keywords = models.CharField(max_length=255)
    movie_imdb_link = models.CharField(max_length=255)
    num_user_for_reviews = models.IntegerField()
    language = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    content_rating = models.CharField(max_length=255)
    budget = models.IntegerField()
    title_year = models.IntegerField()
    # actor_2_facebook_likes = models.CharField(max_length=255)
    imdb_score = models.FloatField()
    # aspect_ratio = models.CharField(max_length=255)
    # movie_facebook_likes = models.CharField(max_length=255)

    def __str__(self):
        return self.movie_title + ' - ' + self.title_year


