from tabnanny import verbose
from django.db import models

class User(models.Model):

    username = models.CharField(max_length=128, verbose_name = '이름')
    birthday = models.CharField(max_length=128, verbose_name='생년월일')
    phoneNum = models.CharField(max_length=128, verbose_name='휴대폰번호')
    email = models.EmailField(max_length=128, verbose_name='이메일')
    userId = models.CharField(max_length=128, verbose_name = '아이디')
    password = models.CharField(max_length=128, verbose_name = '비밀번호')

    class Meta:
        db_table = 'movie_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자(들)'
    
    def __str__(self):
        return f'{self.username}'
