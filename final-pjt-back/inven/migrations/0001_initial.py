# Generated by Django 3.2.13 on 2022-11-22 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviecount',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
