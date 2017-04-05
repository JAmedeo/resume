from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect






urlpatterns = patterns('',
	url(r'^$', lambda r: HttpResponseRedirect('home/')),
	url(r'^home/', include('japp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)