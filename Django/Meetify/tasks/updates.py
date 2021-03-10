from ..celery import app
from ..models import User_Info
from ..appapi import users as u


@app.task
def update_user_data():
    users = User_Info.objects.filter(SpotifyUserId__isnull=False)
    for user in users:
        token = u.refresh_token(user.SpotifyAuthToken)
        u.update_liked_songs(user.pk, token)
        u.update_user_audio_features_scores(user.pk, token)
        u.update_user_matches(user.pk, token)