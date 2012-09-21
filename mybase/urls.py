from django.conf.urls import patterns, include, url
from main.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mybase.views.home', name='home'),
    # url(r'^mybase/', include('mybase.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^clients/$', ClientList.as_view(), name='clients_list'),
    url(r'^clients/(?P<pk>\d+)/$', ClientDetail.as_view(), name='client_detail'),
)