from django.core.mail import send_mail, EmailMessage, mail_admins, BadHeaderError
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from .tasks import notify_customers
import logging
from rest_framework.views import APIView
import requests


# # sending mails to clients
# def say_hello(request):
#     try:
#         send_mail('subject', 'message', 'from email i.e com.qandeelhaider@gmail.com', ['list of recipients i.e haider@mail.com'])
#     except BadHeaderError:
#         pass 
#     return render(request, 'hello.html', {'name': 'Qandeel'})
#----#

# # sending mails to admins(penal)
# def say_hello(request):
#     try:
#         mail_admins('this is subject', 'this is acutal message', html_message='the html message')
#     except BadHeaderError:
#         pass 
#     return render(request, 'hello.html', {'name': 'Qandeel'})
# # in settings.py
# # ADMINS = [
# #     ('Haider', 'admin@haiderbuy.com')
# # ]
#----#

# # sending mails (if we want more control on mails like attachments or adding bcc or cc feature)
# def say_hello(request):
#     try:
#         message = EmailMessage('this is subject', 'this is acutal message', 
#                                'from ie haider@mail.com', ['list of recipeints ie abc@mail.com'])
#         message.attach_file('playground/static/images/dog.jpg')
#         message.send()
#     except BadHeaderError:
#         pass 
#     return render(request, 'hello.html', {'name': 'Qandeel'})
#----#

# sending mails (using django-templated-mail which extends the django EmailMessage class) we can use complete template based emails here
# def say_hello(request):
#     try:
#         message = BaseEmailMessage(
#             template_name='emails/hello.html',
#             context={'name': 'Haider'}
#         )
#         message.send(['recipient list i.e haider@haiderbuy.com'])
#     except BadHeaderError:
#         pass 
#     return render(request, 'hello.html', {'name': 'Qandeel'})
# #----#

# # celery task
# def say_hello(request):
#     notify_customers.delay('Hello')
#     return render(request, 'hello.html', {'name': 'Haider'})

# ---- #

# # demo func just for testing logging functionality

logger = logging.getLogger(__name__)

class HelloView(APIView):
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Haider'})
