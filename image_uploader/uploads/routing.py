from django.urls import re_path
from .consumers import ImageConsumer

websocket_urlpatterns = [
    re_path(r'ws/images/(?P<image_id>\d+)/$', ImageConsumer.as_asgi()),
]
