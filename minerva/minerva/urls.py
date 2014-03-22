from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authentication.urls')),

    url(r'^$', 'minerva.views.index', name='index'),
    url(r'^view1/$', 'minerva.views.view1', name='view1'),
    url(r'^view2/$', 'minerva.views.view2', name='view2'),
    url(r'^view3/$', 'minerva.views.view3', name='view3'),
    
)
