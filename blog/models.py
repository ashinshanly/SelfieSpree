from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.urlresolvers import reverse


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



class UserProfile(models.Model):
    #docstring for ClassName
    user = models.OneToOneField(User)
    email = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    bio = models.CharField(max_length=1000, default='')

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
   if kwargs['created']:
      user_profile = UserProfile.objects.create(user = kwargs['instance'])


post_save.connect(create_profile, sender=User) 
    














"""# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils import timezone

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class SignUp(models.Model):
    full_name= models.CharField(max_length=120)
    email=models.EmailField()
    timestamp=models.DateField(auto_now_add=True,auto_now=False)
    updated=models.DateField(auto_now_add=False,auto_now=True)
    def __unicode__(self):
        return self.email
# Create your models here.

class Picto(models.Model):
    image_id  = models.AutoField(primary_key=True)
    user   = models.ForeignKey(User)
    image  = models.FileField()
    like  = models.IntegerField(default=0) 
    def get_absolute_url(self):
        return reverse('home') 
    def __unicode__(self):
        return unicode(self.user)

class userlike(models.Model):
    like_id=models.AutoField(primary_key=True)
    image_id = models.IntegerField()
    user   = models.ForeignKey(User)
    favourite = models.BooleanField(default="False") 
    def __unicode__(self):
            return unicode(self.user)



class Profile(models.Model):
    #docstring for ClassName
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    pic =   models.FileField()
    city = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    bio = models.CharField(max_length=500, default='')
    def __unicode__(self):
            return unicode(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile,sender=User) """



