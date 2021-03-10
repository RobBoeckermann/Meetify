from celery.schedules import crontab
from ..celery import app
from .updates import *


@app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    # Update user data (Daily @ 6:00AM UTC / 1:00AM EST)
    sender.add_periodic_task(crontab(hour=6), update_user_data.s(), name='Update user data')

