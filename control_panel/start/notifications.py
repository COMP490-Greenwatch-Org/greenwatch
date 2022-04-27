from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

from email.mime.image import MIMEImage
from django.contrib.staticfiles import finders
from functools import lru_cache
from django.templatetags.static import static




#user information is passed through request
#title and body are strings
#att is the an image object
def notify(request, title="Default title", body="Default body", att=None):
    template = render_to_string('start/email_notification.html', {'name': request.user.first_name, 'body':body })
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

#my mess
def notify2(request, title="Default title", body="Default body", att=None):
    
    title = "Lawn health Status"
    
    context = {
    'first_name': request.user.first_name,
    'img_name' : att.name,
    'img_results': att.results,
    'img_date' : att.date,
    'body': body,
    }
    
    template = render_to_string('start/email_notification.html', context)
    email = EmailMessage(
        subject = title,#The subject line of the email.
        body = template,#The body text. This should be a plain text message.
        from_email = settings.EMAIL_HOST_USER,#From. The sender’s address.
        to = [request.user.email],#To. A list or tuple of recipient addresses.    
        #attachments = (A list of attachments to put on the message. These can be
        # either MIMEBase instances, or (filename, content, mimetype) triples.)
    )
    email.content_subtype = "html"  # Main content is now text/html
    
    email.fail_silently = False
    if att:
        email.attach(att.image.name, att.image.read())
    email.send()











#my messier mess
@lru_cache()
def logo_data():
    url = static('static/greenwatch_logo.png')
    with open(url, 'rb') as f:
        logo_data = f.read()
    logo = MIMEImage(logo_data)
    logo.add_header('Content-ID', '<logo>')
    return logo

def notify3(request, title="Lawn health Status", body="Default body", att=None):
    
   
    
    
    body_html  = """<html><img src="cid:logo" alt="logo image"></html>"""
    
    message = EmailMultiAlternatives(
        subject = title,#The subject line of the email.
        body = body,#The body text. This should be a plain text message.
        from_email = settings.EMAIL_HOST_USER,#From. The sender’s address.
        to = [request.user.email],#To. A list or tuple of recipient addresses.    
        #attachments=attachments #(A list of attachments to put on the message. These can be
        # either MIMEBase instances, or (filename, content, mimetype) triples.)
        
    )
    message.mixed_subtype = 'related'
    message.attach_alternative(body_html, "text/html")
    message.attach(logo_data())

    message.send(fail_silently=False)

           
    


