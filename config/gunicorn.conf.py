import platform
import os

# bind = "0.0.0.0:8000": not considered to be good way in terms of performance, thi unix sock provide way faster and smoother experience.
# DJANGO_SETTINGS_MODULE = "lifesyncnow_backend.settings.dev"

# worker_class = "sync"
# proc_name = "lifesyncnow_backend"
# raw_env = [
#     "ASGI_THREADS=4",
#     "ASGI_WORKER_CLASS=daphne.worker.Worker",
# ]

socket_dir = os.environ.get('SOCKET_DIR', '/run')
bind = f'unix:{socket_dir}/gunicorn.sock'
worker_class = 'gthread'
workers = 1
# bind = '/media/qandeel/Drive0/programs/full-stack/LifeSyncNow/lifesyncnow-backend/var/run/gunicorn.sock'
# system = platform.system()
# if system == 'Linux':
#     bind = 'unix:/media/qandeel/Drive0/programs/full-stack/LifeSyncNow/lifesyncnow-backend/var/run/gunicorn.sock'
#     print(f'Using Linux path: {bind}')
# elif system == 'Darwin':  # macOS
#     bind = 'unix:/usr/local/var/run/gunicorn.sock'
#     print(f'Using macOS path: {bind}')
# else:
#     # For other operating systems, specify a fallback path
#     bind = 'unix:/path/to/gunicorn.sock'
#     print(f'Using fallback path: {bind}')
