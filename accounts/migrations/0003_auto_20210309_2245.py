# Generated by Django 3.1.6 on 2021-03-09 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210309_0731'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='subscribe',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 9, 22, 45, 47, 146441)),
        ),
    ]
