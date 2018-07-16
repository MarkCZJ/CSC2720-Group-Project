import csv
from movies.models import Movie

# Movie.objects.all().delete()

with open(r'D:\Dropbox\MovieRatings\imdb_movies.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    next(reader, None)
    for row in reader:
        _, created = Movie.objects.get_or_create(
            director_name=row[0],
            duration=row[1],
            actor_2_name=row[2],
            gross=row[3],
            genres=row[4],
            actor_1_name=row[5],
            movie_title=row[6],
            num_voted_users=row[7],
            actor_3_name=row[8],
            movie_imdb_link=row[9],
            num_user_for_reviews=row[10],
            language=row[11],
            country=row[12],
            content_rating=row[13],
            budget=row[14],
            title_year=row[15],
            imdb_score=row[16],
        )


        # tconst=row[0],
        # primaryTitle=row[1],
        # startYear =row[2],
        # runtimeMinutes=row[3],
        # genres =row[4],
        # color = row[0],
        # director_name= row[1],
        # num_critic_for_reviews= row[2],
        # duration = row[3],
        # director_facebook_likes = row[4],
        # actor_3_facebook_likes = row[5],
        # actor_2_name = row[6],
        # actor_1_facebook_likes = row[7],
        # gross = row[8],
        # genres = row[9],
        # actor_1_name = row[10],
        # movie_title = row[11],
        # num_voted_users = row[12],
        # cast_total_facebook_likes = row[13],
        # actor_3_name = row[14],
        # facenumber_in_poster = row[15],
        # plot_keywords = row[16],
        # movie_imdb_link = row[17],
        # num_user_for_reviews = row[18],
        # language = row[19],
        # country = row[20],
        # content_rating = row[21],
        # budget = row[22],
        # title_year = row[23],
        # actor_2_facebook_likes = row[24],
        # imdb_score = row[25],
        # aspect_ratio = row[26],
        # movie_facebook_likes = row[27]