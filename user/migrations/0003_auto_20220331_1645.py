# Generated by Django 3.2.5 on 2022-03-31 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20220330_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.CharField(max_length=128, verbose_name='생년월일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phoneNum',
            field=models.CharField(max_length=128, verbose_name='휴대폰번호'),
        ),
    ]
