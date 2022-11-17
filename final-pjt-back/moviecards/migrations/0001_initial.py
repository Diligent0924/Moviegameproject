# Generated by Django 3.2.13 on 2022-11-17 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('movie_type', models.CharField(max_length=100)),
                ('is_show', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('poster_path', models.CharField(max_length=200)),
                ('attack_damage', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_type', models.CharField(max_length=100)),
                ('skill_range', models.IntegerField()),
                ('skill_comment', models.CharField(default='이 카드는 평범한 카드입니다...', max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card')),
            ],
        ),
        migrations.CreateModel(
            name='NormalCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('poster_path', models.CharField(max_length=200)),
                ('attack_damage', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card')),
            ],
        ),
        migrations.CreateModel(
            name='BossCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('poster_path', models.CharField(max_length=200)),
                ('attack_damage', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card')),
            ],
        ),
    ]
