from django.db import models


# Create your models here.
class News(models.Model):
    news_title = models.CharField(max_length=200, null=False)
    news_content = models.TextField(blank=True)
    news_views = models.IntegerField(default=0)
    news_date = models.DateTimeField(auto_now_add=True)

    admins = models.ForeignKey('user.User', on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'news'

    def __str__(self):
        return f'{self.news_title}'


