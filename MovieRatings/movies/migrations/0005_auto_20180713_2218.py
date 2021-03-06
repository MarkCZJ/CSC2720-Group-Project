# Generated by Django 2.0.7 on 2018-07-14 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actor_1_facebook_likes',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='actor_2_facebook_likes',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cast_total_facebook_likes',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='facenumber_in_poster',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_facebook_likes',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='movie',
            name='num_voted_users',
            field=models.CharField(max_length=255),
        ),
    ]
