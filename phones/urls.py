from django.conf.urls import patterns, url

from phones import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^sendContact$', views.sendContact, name = 'sendContact'),
    url(r'^login$', views.login, name = 'login'),
    url(r'^(?P<user_id>\d+)/logout/$', views.logout, name='logout'),
    url(r'^(?P<user_id>\d+)/myStore/$', views.myStore, name='myStore'),
    url(r'^(?P<user_id>\d+)/productManagement/$', views.productManagement, name='productManagement'),
    url(r'^(?P<user_id>\d+)/accountManagement/$', views.accountManagement, name='accountManagement'),
    url(r'^(?P<user_id>\d+)/dealerHome/$', views.dealerHome, name='dealerHome'),
    url(r'^(?P<user_id>\d+)/(?P<product_id>\d+)/sellProduct/$', views.sellProduct, name='sellProduct'),
    url(r'^#login/$', views.logoutForm, name='logoutForm'),
    )
