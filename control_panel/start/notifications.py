from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


#user information is passed through request
#title and body are strings
#att is the an image object
def notify(request, title="Default title", body="Default body", att=None):
    
    context = {
    'first_name': request.user.first_name,
    'results': att.results,
    'date' : att.date,
    'body': body,
    }
    template = render_to_string('start/email_notification.html', context)
    
    email = EmailMessage(
        title,
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )
    email.fail_silently = False
    if att:
        email.attach(att.image.name, att.image.read())
    email.send()

