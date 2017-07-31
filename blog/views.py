from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Post
from .forms import(
	

	RegistrationForm, 
	EditProfileForm

	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import(

	UserCreationForm,
	UserChangeForm,
	PasswordChangeForm

	) 

from django.contrib.auth import  update_session_auth_hash
from django.contrib.auth.decorators import login_required

from .models import UserProfile



from django.db import transaction

from django.core.mail import send_mail
from django.conf import settings
#from .forms import SignUpForm
#from .forms import ContactForm
#from .models import Picto,userlike,UserProfile
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse



# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def home(request):
	return render(request, 'blog/home.html',{})

def upload(request):
	return render(request, 'blog/upload.html', {})


def index(request):
	return render(request, 'blog/index.html', {})

def home(request):
    return render(request,"blog/home.html")

def events(request):
    return render(request,"blog/events.html")
def hala(request):
    return render(request,"blog/hala.html")

def lightbox(request):
	return render(request,"blog/lightbox.html")


def anim(request):
    return render(request, 'blog/anim.html', {})


def enter(request):
    return render(request,"blog/enter.html")


def about(request):
	return render(request, "blog/about.html")

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('events')

	else:
		form = RegistrationForm()
		args={'form': form}
		return render(request, 'blog/register.html',args)

@login_required
def view_profile(request):
	args={'user':request.user}
	return render(request, 'blog/profile.html', args)
	
@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user.userprofile)
		if form.is_valid():
			form.save()
			return redirect('profile')



	else:
		form = EditProfileForm(instance=request.user.userprofile)
		args={'form': form}
		return render(request,'blog/edit_profile.html', args)


@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profile')
		else:
			return redirect('change-password')


	else:
		form = PasswordChangeForm(user=request.user)
		args={'form': form}
		return render(request,'blog/change_password.html', args) 
















"""# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render,redirect
from .forms import SignUpForm,ContactForm
from .models import Picto,userlike,Profile
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .forms import(
	ProfileForm,UserForm)

	
from django.db import transaction


# Create your views here.
def index(request):
    title="welcome %s" % request.user
    forms = ContactForm(request.POST)
    if forms.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': forms
        }
    return render(request,'blog/index.html',context)

def about(request):
    title = "welcome %s" % request.user
    forms = ContactForm(request.POST)
    if forms.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': forms
    }
    return render(request,"about.html",context)
class EntryCreate(CreateView):
            model=Picto
            template_name="entry.html"
            fields=['user','image']
@login_required
def detail(request):
    title = "welcome %s" % request.user
    forms = ContactForm(request.POST)
    if forms.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': forms
    }
    pro=Picto.objects.all()
    return render(request,"hala.html",{'pro':pro,'forms':forms})
@login_required
def page(request,image_id):
    flag=0
    us=Picto.objects.get(pk=image_id)
    users=userlike.objects.filter(image_id=image_id)
    if users.count() !=0:
        for user in users:
            if user.user==request.user:
                flag=1
                if user.favourite==True:
                    user.favourite=False
                    us.like-=1
                    us.save()
                    user.save()
                else:
                    user.favourite=True
                    us.like+=1
                    us.save()
                    user.save()
                break
        if flag!=1:
                user=userlike()
                user.image_id=image_id
                user.user=request.user
                us.like+=1
                us.save()
                user.favourite=True
                user.save()
    else:
        user=userlike()
        user.image_id=image_id
        user.user=request.user
        us.like+=1
        us.save()
        user.favourite=True
        user.save()
    return redirect("detail")

def events(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'form': form
    }
    return render(request,"blog/events.html",context)
@login_required
def view_profile(request):
	args={'user':request.user}
	return render(request, 'blog/profile.html', args)
	
@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
def about(request):
    title = "welcome %s" % request.user
    forms = ContactForm(request.POST)
    if forms.is_valid():
        form_mail = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        subject = 'site contact form'
        from_email = form_mail
        to_email = [settings.EMAIL_HOST_USER, ]
        contact_message = "Hello %s,Welcome to new era" % form_full_name
        send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
    context = {
        'forms': forms
    }
    return render(request,"about.html",context)
def slide(request):
    pro=Picto.objects.all()
    return render(request,"lightbox.html",{'pro':pro}) """



