from django.conf.urls import url
from myproject.core import views as v

urlpatterns = [
    url(r'^$', v.home, name='home'),
]
