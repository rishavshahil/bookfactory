# Generated by Django 3.1.6 on 2021-03-09 02:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 9, 7, 31, 6, 773046)),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]