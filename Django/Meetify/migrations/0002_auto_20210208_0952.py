# Generated by Django 3.1.6 on 2021-02-08 14:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Meetify', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked_songs',
            name='META_StartDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='matches',
            name='META_StartDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='messages',
            name='META_StartDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='META_StartDate',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
