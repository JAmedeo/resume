from django.conf.urls import *

from japp import views



urlpatterns = patterns('',
	url(r'^$', views.homeView, name = 'japphomeView'),
	)