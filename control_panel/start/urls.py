from xml.etree.ElementInclude import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('settings/',views.settings, name='settings'),
    path('archive/',views.archive, name='archive'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register'),
]