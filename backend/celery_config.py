from celery import Celery
from celery.schedules import crontab
from app.tasks import store_data_tasks, scrape_tasks


celery = Celery('tasks', broker='redis://localhost:6380/0', backend='redis://localhost:6380/0')

celery.conf.beat_schedule = {
    'scrape-vikings-every-5-minutes': {
        'task': 'app.tasks.store_data_tasks.scrape_and_store_vikings',
        'schedule': crontab(minute='*/1'),
    },
    'scrape-norsemen-every-5-minutes': {
        'task': 'app.tasks.store_data_tasks.scrape_and_store_norsemen',
        'schedule': crontab(minute='*/5'),
    },
}

celery.conf.broker_connection_retry = True

celery.conf.timezone = 'UTC'
