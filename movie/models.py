from django.db import models

class Movie(models.Model): # 영화 DB
    movie_code = models.CharField(max_length=100, primary_key=True) # 영화코드
    # 평점 ForignKey
    movie_title = models.CharField(max_length=30) # 영화제목
    movie_overview = models.TextField() # 줄거리
    movie_director = models.CharField(max_length=100) # 감독
    movie_poster = models.CharField(max_length=100) # 포스터
    movie_company = models.CharField(max_length=50) # 제작사
    movie_opendt = models.DateField() # 개봉일

    class Meta:
        db_table = 'movie'

    def __str__(self):
        return f'{self.movie_title}'