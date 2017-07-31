from django.contrib import admin
from .models import Post
from .models import UserProfile


# Register your models here.
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.site_header = 'SelfieSpree Administration'


# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

#from django.contrib import admin

#from .models import SignUp,Picto,userlike,Profile

#class SignUpAdmin(admin.ModelAdmin):
#    list_display=["__unicode__","timestamp","updated"]
#    class Meta:
#s        model= SignUp

#admin.site.register(SignUp,SignUpAdmin)
#admin.site.register(Picto)
#admin.site.register(userlike)
#admin.site.register(Profile)
# Register your models here.
