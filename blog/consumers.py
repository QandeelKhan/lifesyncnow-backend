from channels.generic.websocket import AsyncWebsocketConsumer


class ProgressWebSocket(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'progress_updates'
        print("connect triggered")
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        print("disconnect triggered")
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def progress_update(self, event):
        print("progress update triggered")
        progress = event['progress']
        await self.send(text_data=str(progress))

    async def progress_completed(self, event):
        print("progress complete triggered")
        await self.send(text_data='completed')
