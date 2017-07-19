from django.conf.urls import url
from myproject.core import views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
    url(r'^add/$', v.contact_add, name='contact_add'),
    url(r'^(?P<pk>[^/]+)/delete/$', v.contact_delete, name='contact_delete'),
]
