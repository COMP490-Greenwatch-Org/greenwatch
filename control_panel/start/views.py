from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import ExtendedUserCreationForm

from django.http import HttpResponse

def index(request):
    username = request.user.username
    context = {'username' : username}
    return render(request, 'start/index.html', context)

def settings(request):
    return render(request, 'start/settings.html')

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