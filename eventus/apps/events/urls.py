from django.conf.urls import patterns, url
from .views import IndexView, MainPanelView, CreateEvent, EventDetail, EventEdit, EventDelete

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    
    url(r'^panel/$', MainPanelView.as_view(), name='panel'),
    url(r'^panel/evento/nuevo/$', CreateEvent.as_view(), name='nuevo'),
    url(r'^panel/evento/(?P<pk>\d+)/$', EventDetail.as_view(), name='detalle'),
    url(r'^panel/evento/editar/(?P<pk>\d+)$', EventEdit.as_view(), name='editar'),
    url(r'^panel/evento/eliminar/(?P<pk>\d+)$', EventDelete.as_view(), name='eliminar'),
)