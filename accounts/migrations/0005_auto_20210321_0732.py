# Generated by Django 3.1.6 on 2021-03-21 02:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210321_0421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 3, 21, 7, 32, 19, 730694)),
        ),
    ]
