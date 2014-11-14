from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eventus.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('apps.events.urls', namespace="events_app")),
    url(r'^', include('apps.users.urls', namespace="users_app")),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns("",
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT,}
        ),
    )