# Generated by Django 3.1.5 on 2021-02-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Meetify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_features',
            name='acousticness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='danceability',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='energy',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='instrumentalness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='loudness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='speechiness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='tempo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='audio_features',
            name='valence',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='acousticness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='danceability',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='energy',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='instrumentalness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='loudness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='speechiness',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='tempo',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='matches',
            name='valence',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
