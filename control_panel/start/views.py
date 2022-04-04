from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm, NotificationsForm
from camera.models import Camera, Image
from .notifications import notify

def index(request):
    username = request.user.username
    #cameras = Camera.objects.filter(user=request.user)
    context = {'username' : username}
    return render(request, 'start/index.html', context)

@login_required
def settings(request):
    if request.method =='POST':
        form = NotificationsForm(request.POST, instance=request.user.extendeduser)
        if form.is_valid():
            form.save()
            return redirect('settings')
    else:
        form = NotificationsForm(instance=request.user.extendeduser)
    context = {"form" : form}
    return render(request, 'start/settings.html', context)

@login_required
def archive(request):
    return render(request, 'start/archive.html')

@login_required
def profile(request):
    return render(request, 'start/profile.html')

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = ExtendedUserCreationForm()

    context = {'form' : form}
    return render(request, 'start/register.html', context)