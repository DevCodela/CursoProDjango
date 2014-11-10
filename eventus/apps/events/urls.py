from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'apps.events.views.index', name='index'),

    url(r'^login/$', 'apps.events.views.login', name='login'),
    
    url(r'^panel/$', 'apps.events.views.main_panel', name='panel'),
    url(r'^panel/evento/nuevo/$', 'apps.events.views.crear_evento', name='nuevo'),
    url(r'^panel/evento/(?P<evento_id>\d+)/$', 'apps.events.views.detalle_evento', name='detalle'),
    url(r'^panel/evento/editar/(?P<evento_id>\d+)$', 'apps.events.views.editar_evento', name='editar'),
    url(r'^panel/evento/eliminar/(?P<evento_id>\d+)$', 'apps.events.views.eliminar_evento', name='eliminar'),
)