# Generated by Django 4.1.1 on 2022-09-24 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0007_alter_movie_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='reviews',
        ),
        migrations.AddField(
            model_name='movie',
            name='rev',
            field=models.ManyToManyField(related_name='like', to='movie_app.review'),
        ),
    ]