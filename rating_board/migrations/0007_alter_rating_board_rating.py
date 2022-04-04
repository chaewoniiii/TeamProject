# Generated by Django 3.2.5 on 2022-03-31 05:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating_board', '0006_rating_board_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating_board',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
    ]