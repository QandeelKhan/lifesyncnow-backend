CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        # setting redis database number as 0
        'LOCATION': 'redis://redis:6379/0',
        # 'TIMEOUT': 10 * 60,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CELERYD_LOG_LEVEL = 'CELERY-INFO'
CELERY_APP = 'lifesyncnow_backend.celery_app'
DEFENDER_CACHE = 'default'
BROKER_URL = 'redis://redis:6379/0'
REDIS_URL = 'redis://redis:6379/0'
# Celery Broker settings
# Update with your Redis configuration
# Specifying the Redis connection URL for Celery's broker.
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_CACHE_BACKEND = 'default'  # Use the default cache backend for Celery
CELERY_BACKEND_URL = 'redis://redis:6379/0'
# Flower Configuration (flower is used to monitor celery tasks in browser)
CELERY_FLOWER_PORT = 5555
# CELERY_RESULT_BACKEND = 'django-db'  # Use Django database as the result backend
# but i already have redis configured so celery is not alone,and we intended to use Redis as the result backend instead of
DEFENDER_REDIS_URL = "redis://redis:6379/1"

# CELERY_FLOWER_USER = '<flower-username>'
# CELERY_FLOWER_PASSWORD = '<flower-password>'
# run commands:
# 1st approach: celery -A lifesyncnow_backend.settings.dev flower
# 2nd approach: celery --app=lifesyncnow_backend.settings.dev --settings=lifesyncnow_backend.settings.dev flower
