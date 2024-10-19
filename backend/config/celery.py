from celery import Celery
import os
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'send-reminder-every-hour': {
        'task': 'appointments.tasks.appointment_notif',
        'schedule': crontab(minute=0, hour='*'),  
    },
}

app.conf.timezone = 'UTC'