import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ImageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.image_id = self.scope['url_route']['kwargs']['image_id']
        self.image_group_name = f'image_{self.image_id}'
        await self.channel_layer.group_add(self.image_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.image_group_name, self.channel_name)

    async def image_processed(self, event):
        await self.send(text_data=json.dumps(event))
