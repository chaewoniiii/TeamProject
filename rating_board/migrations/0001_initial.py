# Generated by Django 3.2.5 on 2022-04-06 00:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('movie', '0001_initial'),
        ('user', '0003_auto_20220331_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating_Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating_content', models.TextField(blank=True)),
                ('rating', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
                ('movie_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'rating_board',
            },
        ),
    ]
