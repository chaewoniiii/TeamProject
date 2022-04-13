from pyexpat import model
from django.db import models

# Create your models here.
class Payinfo(models.Model):
    people = models.IntegerField(default=1)
    price = models.IntegerField(default=0)

    user = models.OneToOneField('user.User', on_delete=models.CASCADE)
    movie = models.OneToOneField('movie.Movie', on_delete=models.CASCADE)

    class Meta:
        db_table = 'payinfo'

    def __str__(self) -> str:
        return super().__str__()