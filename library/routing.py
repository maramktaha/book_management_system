from django.urls import path
from .consumers import BookNotificationConsumer

websocket_urlpatterns = [
    path('ws/book_notifications/', BookNotificationConsumer.as_asgi()),
]
