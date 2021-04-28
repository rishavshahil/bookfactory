# Generated by Django 3.1.6 on 2021-02-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='books/image')),
            ],
        ),
    ]