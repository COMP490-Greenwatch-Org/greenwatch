from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import CamForm, ExtendedUserCreationForm, NotificationsForm, UserUpdateForm
from camera.models import Camera, Image

from .notifications import notify, notify2
from django.core.paginator import Paginator

def index(request):
    username = request.user.username
    #cameras = Camera.objects.filter(user=request.user)
    context = {'username' : username}
    return render(request, 'start/index.html', context)

@login_required
def profile(request):
    if request.method =='POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        n_form = NotificationsForm(request.POST, instance=request.user.extendeduser)
        form = CamForm(request.POST)
        if u_form.is_valid() and n_form.is_valid() and form.is_valid():
            u_form.save()
            n_form.save()
            form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        n_form = NotificationsForm(instance=request.user.extendeduser)
        form = CamForm()

    context = {"u_form" : u_form, "n_form" : n_form, "form" : form}
    return render(request, 'start/profile.html', context)

@login_required
def archive(request):
    imagelist = Image.objects.all()

    the_image = Paginator(imagelist, 3)

    grouped_images = []
    for page in the_image.page_range:
        image_objects = the_image.page(page).object_list
        grouped_images.append(image_objects)

    context = {'the_image' : the_image, 'grouped_images' : grouped_images}
    return render(request, 'start/archive.html', context)

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

def about(request):
        return render(request, 'start/about.html')


def contact(request):
    #temp method for testing functionality
    if request.method == 'POST':
        contact_name = request.POST['contact-name']
        contact_email = request.POST['contact-email']
        contact_msg = request.POST['contact-msg']
        
        return render(request, 'start/contact.html', {'contact_name':contact_name})
        
    else:
        return render(request, 'start/contact.html')
    
#Temporary page for testing functionality    
def testing(request):
    
    if request.method == 'POST':
        
        the_image = Image.objects.get(pk=1)
        
        notify2(request, att=the_image)
        return render(request, 'start/testing.html')
    
    else:    
        the_image = Image.objects.get(pk=1)
        context = {'the_image' : the_image}
        return render(request, 'start/testing.html', context)