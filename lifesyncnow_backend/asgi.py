import blog.routing
import os

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "lifesyncnow_backend.settings")
# Initialize Django ASGI application early to ensure the AppRegistry


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": (URLRouter(blog.routing.websocket_urlpatterns)),
    }
)
