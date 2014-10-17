import os 

from django.conf import settings
from django.conf.urls import patterns, url

from meraki_inv import views

urlpatterns = patterns('',
            url(r'^$', \
                    views.DeviceList.as_view(), name='device_list'),
            url(r'^device/$', \
                    views.DeviceList.as_view(), name='device_list'),
            url(r'^device/add/$', 
                views.DeviceCreate.as_view(), name='device_add'),
            url(r'^device/(?P<serial>[^/]+)/$', \
                    views.DeviceDetail.as_view(), name='device_item'),
            url(r'^device/(?P<serial>[^/]+)/delete/$', \
                    views.DeviceDelete.as_view(), name='device_delete'),
            url(r'^device/(?P<serial>[^/]+)/edit/$', \
                    views.DeviceEdit.as_view(), name='device_edit'),
            url(r'^device/(?P<serial>[^/]+)/note/$', \
                    views.NoteList.as_view(), name='note_list'),
            url(r'^device/(?P<serial>[^/]+)/note/add/$', \
                    views.NoteCreate.as_view(), name='note_add'),
            url(r'^device/(?P<serial>[^/]+)/note/(?P<note_id>\d+)/$', \
                    views.NoteDetail.as_view(), name='note_item'),
            url(r'^device/(?P<serial>[^/]+)/note/(?P<note_id>\d+)/delete/$', \
                    views.NoteDelete.as_view(), name='note_delete'),
            url(r'^device/(?P<serial>[^/]+)/note/(?P<note_id>\d+)/edit/$', \
                    views.NoteEdit.as_view(), name='note_edit'),
            url(r'^device/(?P<serial>[^/]+)/status/$', \
                    views.StatusCreate.as_view(), name='status_create'),
            url(r'^device/(?P<serial>[^/]+)/return/$', \
                    views.StatusUpdate.as_view(), name='status_edit'),
            )
