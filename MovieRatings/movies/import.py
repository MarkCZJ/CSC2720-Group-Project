import csv
from movies.models import Movie

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