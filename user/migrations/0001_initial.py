# Generated by Django 3.2.5 on 2022-03-30 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64, verbose_name='이름')),
                ('birthday', models.IntegerField(default=0, verbose_name='생년월일')),
                ('phoneNum', models.IntegerField(default=0, verbose_name='휴대폰번호')),
                ('email', models.EmailField(max_length=128, verbose_name='이메일')),
                ('userId', models.CharField(max_length=64, verbose_name='아이디')),
                ('password', models.CharField(max_length=64, verbose_name='비밀번호')),
            ],
            options={
                'verbose_name': '사용자',
                'verbose_name_plural': '사용자(들)',
                'db_table': 'movie_user',
            },
        ),
    ]
