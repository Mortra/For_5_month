# Generated by Django 4.1.1 on 2022-09-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0013_alter_review_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rev',
            field=models.ManyToManyField(null=True, related_name='like', to='movie_app.review'),
        ),
    ]
