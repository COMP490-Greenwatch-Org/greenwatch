from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

def notify(request, title="Default title", body="Default body", att=None):
    template = render_to_string('start/email_notification.html', {'name': request.user.first_name, 'body':body})
    email = EmailMessage(
        title,
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently = False
    if att:
        #will implement attachments from database once the camera and image models are ready
        email.attach_file('start/static/start/greenwatch_logo.png')
    
    email.send()
