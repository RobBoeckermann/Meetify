<<<<<<< Updated upstream
# from channels.generic.websockets import WebsocketConsumer
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# from models import Messages


# class ChatConsumer(WebsocketConsumer):

#     def connect(self, message, **kwargs):
#         self.user_id = int(kwargs['user_id'])
#         self.messages = list(Messages.objects.filter(MatchId_id.User1=self.user_id) | Messages.objects.filter(MatchId_id.User2=self.user_id))

#         self.message.reply_channel.send({"accept": True})

#     def disconnect(self, message, **kwargs):
#         pass

#     @receiver(post_save, sender=Messages)
#     def chat(self, sender, **kwargs):
#         if kwargs['instance'].MatchId_id.User1 == self.user_id or kwargs['instance'].MatchId_id.User2 == self.user_id:
#             self.messages = list(kwargs['instance'])
#             print(messages[0].pk)

#     def receive()
