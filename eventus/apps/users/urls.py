from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^login/$', 'apps.users.views.userlogin', name="login"),
	url(r'^salir/$', 'apps.users.views.LogOut', name = 'logout')
)