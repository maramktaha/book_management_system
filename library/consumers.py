import json
from channels.generic.websocket import AsyncWebsocketConsumer

class BookNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Create a group name for book notifications (can be per user, per book, or a general one)
        self.group_name = "book_notifications"
        
        # Join the group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        

        await self.accept()

    async def disconnect(self, close_code):
        # Leave the group when WebSocket is disconnected
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )


    async def send_book_notification(self, event):
        message = event['message']
   

        # Send the message to the WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
