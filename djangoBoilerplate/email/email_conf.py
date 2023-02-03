from django.conf import settings
from decouple import config

LOGIN_REDIRECT_URL = '/profile/'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp4dev'
EMAIL_PORT = 2525
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = config('EMAIL_HOST_USER')
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = ''

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
