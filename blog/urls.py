from django.conf.urls import url 
from . import views
from django.contrib.auth.views import(


    login, 
    logout, 
    password_reset, 
    password_reset_done,
    password_reset_confirm,
    password_reset_complete


    )

from django.conf import settings
from django.conf.urls.static import static

from django.core.urlresolvers import reverse
from django.urls import reverse



urlpatterns = [  
   # url(r'^$', views.post_list, name = 'post_list'),

    url(r'^login/$', login, {'template_name': 'blog/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'blog/logout.html'}),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit$', views.edit_profile, name='edit_profile'),
    url(r'^profile/edit/change-password$', views.change_password, name='change_password'),
    url(r'^profile/edit/reset-password$', password_reset, {'template_name': 'blog/reset_password.html'}),
    url(r'^profile/edit/reset-password/done$', password_reset_done, {'template_name': 'blog/reset_password_done.html'}),
    url(r'^profile/edit/reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, name='password_reset_confirm'),
    url(r'^profile/edit/reset-password/complete$', password_reset_complete, name='password_reset_complete'),

    url(r'^upload$', views.upload, name='upload'),
    url(r'^index$', views.index, name='index'),

    
    url(r'^events/$', views.events, name = 'events'),
   
    url(r'^hala$', views.hala, name='hala'),
    url(r'^enter$', views.enter, name='enter'),
    url(r'^about/$', views.about, name='about'),
    url(r'^lightbox$', views.lightbox, name='lightbox'),


    url(r'^anim$', views.anim, name='anim'),



] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 


"""from django.contrib import admin
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views as views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^admin/', admin.site.urls),
    
    url(r'^about/$',views.about,name="about"),
    url(r'^events/$', views.events, name='events'),
    url(r'^$', views.index, name='index'),   
       
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^add$', views.EntryCreate.as_view(), name='addentry'),
    url(r'^page/(?P<image_id>[0-9]+)/$', views.page, name='pages'),
    url(r'^page/$', views.detail, name='detail'),
        
    url(r'^profile$', views.view_profile, name='profile'),
    url(r'^profile/edit$', views.update_profile, name='edit_profile'),
    url(r'^about/$', views.about, name='about'),

   
]

if settings.DEBUG:
        urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
        urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  """ 
