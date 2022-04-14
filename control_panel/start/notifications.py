from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


#user information is passed through request
#title and body are strings
#att is the an image object
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
        email.attach(att.image.name, att.image.read())
    email.send()

#same as notify for now but want to implement an email base template to go with the registration,
# password reset, and notification emails.
def notify2(request, title="Default title", body="Default body", att=None):
    html = render_to_string('auth_app/email/welcome.html', [request.user.email])
    text = render_to_string('auth_app/email/welcome.txt', [request.user.email])
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