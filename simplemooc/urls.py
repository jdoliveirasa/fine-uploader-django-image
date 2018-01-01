"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path

from simplemooc.core import urls   
import simplemooc.core.views 
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = [
	### url(r'^$', 'simplemooc.core.views.home', name='home'),
	url(r'^$', simplemooc.core.views.home, name='home'),  
	url(r'^contato/$', simplemooc.core.views.contact, name='contact'), 
    url(r'^fileupload/$', simplemooc.core.views.fileupload, name='fileupload'),
    url(r'^fineupload/$', simplemooc.core.views.fineupload, name='fineupload'), 
    url(r'^post/$', simplemooc.core.views.post, name='post'), 
    url(r'^uploads/$', simplemooc.core.views.uploads, name='uploads'), 
    url(r'^uploadsdelete/(?P<uuid>[^/]+)/$', simplemooc.core.views.uploadsdelete, name='uploadsdelete'), 
    #url(r'^', include(urls, name='home')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
