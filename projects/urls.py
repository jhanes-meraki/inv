from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meraki_inv/', include('meraki_inv.urls', namespace="meraki_inv")),
)
