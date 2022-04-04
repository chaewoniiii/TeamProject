from django.db import models

class Ticket(models.Model):
    pay = models.IntegerField()
    number_people = models.IntegerField()

    userId = models.ForeignKey('user.User', on_delete=models.CASCADE)
    movie_code = models.ForeignKey('movie.Movie', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'ticket'

    def __str__(self):
        return super().__str__()




