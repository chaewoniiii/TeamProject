# Generated by Django 3.2.5 on 2022-03-30 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='비밀번호'),
        ),
        migrations.AlterField(
            model_name='user',
            name='userId',
            field=models.CharField(max_length=128, verbose_name='아이디'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=128, verbose_name='이름'),
        ),
    ]