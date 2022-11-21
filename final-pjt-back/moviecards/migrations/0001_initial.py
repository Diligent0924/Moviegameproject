from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BossCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('posterpath', models.CharField(max_length=200)),
                ('attackdamage', models.IntegerField()),
                ('hp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('movieid', models.IntegerField(primary_key=True, serialize=False)),
                ('movietype', models.CharField(max_length=100)),
                ('isshow', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UniqueCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('posterpath', models.CharField(max_length=200)),
                ('attackdamage', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card')),
            ],
        ),
        migrations.CreateModel(
            name='UniqueSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skilltype', models.CharField(max_length=100)),
                ('skillrange', models.IntegerField()),
                ('skillcomment', models.CharField(default='이 카드는 평범한 카드입니다...', max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.uniquecard')),
            ],
        ),
        migrations.CreateModel(
            name='NormalCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('posterpath', models.CharField(max_length=200)),
                ('attackdamage', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card')),
            ],
        ),
        migrations.CreateModel(
            name='BossSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skilltype', models.CharField(max_length=100)),
                ('skillrange', models.IntegerField()),
                ('skillcomment', models.CharField(default='이 카드는 평범한 카드입니다...', max_length=100)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.bosscard')),
            ],
        ),
        migrations.AddField(
            model_name='bosscard',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moviecards.card'),
        ),
    ]
