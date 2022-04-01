from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Rating_Board(models.Model):
    rating_content = models.TextField(blank=True)
    rating = models.FloatField(default=0,
                validators=[
                    MaxValueValidator(5),
                    MinValueValidator(0)
                ]
            )

    userId = models.ForeignKey('user.User', on_delete=models.CASCADE)
    # movie_code = models.ForeignKey()

    class Meta:
        db_table = 'rating_board'


    def __str__(self) -> str:
        return super().__str__()
        

