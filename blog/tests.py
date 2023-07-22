from channels.testing import WebsocketCommunicator
from django.test import TestCase
from blog.consumers import ProgressWebSocket


# class ProgressWebSocketTest(TestCase):
#     async def test_progress_update(self):
#         communicator = WebsocketCommunicator(ProgressWebSocket.as_asgi(
#         ), "/ws/progress/d23e26f1-a546-46a0-a3e0-736c885afb9e/")
#         connected, _ = await communicator.connect()
#         self.assertTrue(connected)

#         # Send a test message to the consumer
#         await communicator.send_json_to({"type": "receive", "text": "Test message"})

#         # Receive the response from the consumer
#         response = await communicator.receive_json_from()

#         # Assert the response
#         self.assertEqual(response, {"progress": 50})  # Example assertion

#         await communicator.disconnect()
