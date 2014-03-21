from django.conf.urls import patterns, url
from authentication import views

urlpatterns = patterns('',
    url(r'^login/$', 'authentication.views.user_login', name='login'),
    url(r'^register/$', 'authentication.views.register', name='register'),
    url(r'^logout/$', 'authentication.views.user_logout', name='logout'),
    # url(r'^forgot/$', 'authentication.views.forgot', name='forgot'),

	url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/auth/password/reset/done/', 'template_name' : 'authentication/password_reset_form.html', 'email_template_name' : 'authentication/password_reset_email.html'}, name="password_reset"),
    url(r'^password/reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name' : 'authentication/password_reset_done.html'}),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/auth/password/done/', 'template_name' : 'authentication/password_reset_confirm.html'}),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete', {'template_name' : 'authentication/password_reset_complete.html'}),
)

