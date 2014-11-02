from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.views.generic.base import RedirectView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', RedirectView.as_view(url='meraki_inv/', permanent=False)),
    url(r'^accounts/login/', login, \
            {'template_name': 'meraki_inv/login.html'}, name='login'),
    url(r'^accounts/logout/', logout, \
            {'next_page': '/meraki_inv/'}, name='logout'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^meraki_inv/', include('meraki_inv.urls', namespace="meraki_inv")),
)
