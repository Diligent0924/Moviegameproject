# Generated by Django 3.2.13 on 2022-11-22 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.IntegerField()),
                ('user', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('movietype', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('posterpath', models.CharField(max_length=200)),
                ('attackdamage', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('skillcomment', models.CharField(default='이 카드는 평범한 카드입니다...', max_length=100)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.board')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoreboard.board')),
            ],
        ),
    ]
