from django.conf.urls import patterns, include, url


urlpatterns = patterns('accounts.views',
	url(r'^login/$', 'login'),
	url(r'^auth/$', 'auth_view'),
	url(r'^logout/$', 'logout'),
	url(r'^loggedin/$', 'loggedin'),
	url(r'^invalid/$', 'invalid'),
	url(r'^register/$', 'register_user', name='register_user'),
	url(r'^registered/$', 'registered'),
)
