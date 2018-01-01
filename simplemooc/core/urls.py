from django.conf.urls import url

import simplemooc.core.views  

urlpatterns = [
    url(r'^$', simplemooc.core.views.home, name='home'), 
    url(r'^contato/$', simplemooc.core.views.contact, name='contact'),
    url(r'^fileupload/$', simplemooc.core.views.fileupload, name='fileupload'),
]