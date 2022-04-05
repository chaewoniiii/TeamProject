from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField() # 영화코드가 없는 관계로 id
    title    = models.CharField(max_length=100) # 제목
    released_date = models.CharField(max_length=50) # 개봉일
    popularity = models.FloatField() # 인기
    vote_avg = models.FloatField() # 평점
    overview = models.TextField() # 줄거리
    poster_path = models.CharField(max_length=150) # 포스터
    genres = models.CharField(max_length=50) # 장르 (id값으로만 나와있어 어떻게할지 고민중)
    actors = models.JSONField(null=True) # 배우들
    director = models.CharField(max_length=100, null=True) # 감독 (필드밖에 있어 쓸수있을지 모르겠음) 제작사는 가져오는 API에 없어서 뺐습니다

    class Meta:
        db_table = 'movie'


    def __str__(self):
        return f'{self.title}'