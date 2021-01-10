from django.db import models


class Liked_Songs(models.Model):
    user_id = models.CharField(max_length=200)
    song_id = models.CharField(max_length=200)

    def __str__(self):
        return self.user_id
