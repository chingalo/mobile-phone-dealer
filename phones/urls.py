from django.conf.urls import patterns, url

from phones import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    
    
    )
