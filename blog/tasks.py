import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import BlogPost
from time import sleep
from celery import shared_task
from django.core.cache import cache
# from lifesyncnow_backend.celery_app import app
import logging
logger = logging.getLogger(__name__)


@shared_task
def clear_blogpost_list_cache():
    logger.info("Clearing blogpost_list cache...")
    cache.delete('blogpost_list')


@shared_task
def clear_blogpost_detail_cache(slug):
    cache_key = f'blogpost_detail_{slug}'
    cache.delete(cache_key)


@shared_task
def notify_customers(message):
    print('Sending 10k emails...')
    print(message)
    sleep(10)
    print('Email were successfully sent!')


@shared_task(bind=True)
def load_posts_task(self):
    channel_layer = get_channel_layer()
    progress = 0
    total_posts = 100

    # Load posts logic
    total_posts = 100  # Total number of posts
    for post_num in range(1, total_posts + 1):
        # Load post logic
        time.sleep(0.1)  # Simulate post loading time

        # Calculate progress
        progress = int((post_num / total_posts) * 100)

        # Send progress update
        async_to_sync(channel_layer.group_send)(
            "progress_updates",
            {
                "type": "progress.update",
                "progress": progress,
            },
        )

    # Task completed
    async_to_sync(channel_layer.group_send)(
        "progress_updates",
        {
            "type": "progress.completed",
        },
    )

    return 'All posts loaded successfully'
