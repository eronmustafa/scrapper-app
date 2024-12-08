from celery import Celery

# Initialize Celery
celery = Celery(
    'tasks',
    broker='redis://localhost:6380/0',
    backend='redis://localhost:6380/0'
)

# Import task modules to register tasks
import app.tasks.store_data_tasks
import app.tasks.scrape_tasks
