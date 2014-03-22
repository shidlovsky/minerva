from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'minerva.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include('authentication.urls')),

    url(r'^$', 'app.views.index', name='index'),
    url(r'^view1/$', 'app.views.view1', name='view1'),
    url(r'^view2/$', 'app.views.view2', name='view2'),
    url(r'^view3/$', 'app.views.view3', name='view3'),
    url(r'^api/classes/$', 'app.views.appliance_classes', name='appliance_classes'),
    url(r'^api/types/(?P<appliance_class>\w{0,30})$', 'app.views.appliance_types', name='appliance_types'),
    url(r'^api/usage/$', 'app.views.usage', name='usage'),
    
)
