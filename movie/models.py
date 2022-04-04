from django.db import models

class Movie(models.Model): # 영화 DB
    movie_id = models.IntegerField()
    title    = models.CharField(max_length=100)
    released_date = models.CharField(max_length=50)
    popularity = models.FloatField()
    vote_avg = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=150)
    genres = models.CharField(max_length=50)

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return f'{self.movie_title}'