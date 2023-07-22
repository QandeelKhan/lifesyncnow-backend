import os
from celery import Celery

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'lifesyncnow_backend.settings.dev')

# Create an instance of the Celery application.
app = Celery('lifesyncnow_backend')
# app = Celery('mysite', backend='redis', broker='redis://redis:6379')

# Configure the Celery application.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load tasks from all registered Django app configs.
app.autodiscover_tasks()

# Optional: Add additional configuration if needed.
# For example, setting up a result backend or custom task queues.

# Define the Celery worker's main entry point.


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
