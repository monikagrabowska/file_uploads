from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from files import views

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^s3direct/', include('s3direct.urls')),
    url(r'', include('files.urls')), 
    url(r'^login/$', auth_views.login, name='login'),
]

