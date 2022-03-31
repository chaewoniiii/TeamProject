from django.db import models


# Create your models here.
class Rating_Board(models.Model):
    rating_content = models.TextField(blank=True)
    rating = models.IntegerField(default=0)

    # user_id = models.ForeignKey()
    # movie_code = models.ForeignKey()

    class Meta:
        db_table = 'rating_board'


    def __str__(self):
        return super().__str__()

