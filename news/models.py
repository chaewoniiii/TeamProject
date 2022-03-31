from django.db import models

# Create your models here.
class News(models.Model):
    news_number = models.AutoField(primary_key=True, default=1)
    news_title = models.CharField(max_length=200, null=False)
    news_content = models.TextField(blank=True)
    news_views = models.IntegerField(default=0)
    news_date = models.DateTimeField(auto_now_add=True)

    # admin = models.ForeignKey()

    class Meta:
        db_table = 'news'

    def __str__(self):
        return f'{self.news_title}'


