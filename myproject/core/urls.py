from django.conf.urls import url
from myproject.core import views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^add/$', v.contact_add, name='contact_add'),
    url(r'^(?P<pk>[^/]+)/json/$', v.contact_json, name='contact_json'),
    url(r'^(?P<pk>[^/]+)/edit/$', v.contact_edit, name='contact_edit'),
    url(r'^(?P<pk>[^/]+)/delete/$', v.contact_delete, name='contact_delete'),
]
