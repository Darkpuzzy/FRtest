import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# DOWN CELERY BEAT

# app.conf.beat_schedule = {
#     "added_beat_db_3_min": {
#         'task': 'backend.tasks.added_beat_db',
#         'schedule': crontab(minute=0, hour=0),
#     },
#   }
