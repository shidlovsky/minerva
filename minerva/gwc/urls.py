from django.conf.urls import patterns, url
from django.conf import settings
import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^profile/$', views.profile, name='profile'),
                       url(r'^archive/$', views.profile, name='archive'),
                       url(r'^user/(?P<username>\w+)/$', views.user, name='user'),
                       url(r'^challenge/(?P<challenge_id>\w+)/$', views.challenge, name='challenge'),
                       )