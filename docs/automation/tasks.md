# Automated Tasks

## Setup

### Rabbitmq
- Acts as a broker for automated tasks
- Needs to be running on same machine as tasks
- Can be run on docker:
```
docker run -d -p 5672:5672 rabbitmq
```

### Celery Worker
- Performs the tasks
- Tasks are functions with the `@app.task` decorator and should be located in the `Django/Meetify/tasks` directory
- Start the worker using:
```
celery -A Meetify worker
```

### Celery Beat
- Schedules the tasks
- Periodic tasks are stored in database table named `django_celery_beat_periodictask`
- Add periodic task by adding it to the `setup_periodic_tasks` function in `tasks.py`
- Delete tasks by removing them from the `django_celery_beat_periodictask` table
- *Both celery beat and celery worker need to be running for scheduled tasks to work*
- Start beat using:
```
celery -A Meetify beat --scheduler django_celery_beat.schedulers:DatabaseScheduler
```