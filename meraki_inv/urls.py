import os 

from django.conf import settings
from django.conf.urls import patterns, url

from meraki_inv.views import admin, user

urlpatterns = patterns('',
            url(r'^$', user.DeviceList.as_view(), name='device_list'),
            url(r'^device/$', user.DeviceList.as_view(), name='device_list'),
            url(r'^device/add/$', \
                    admin.DeviceCreate.as_view(), name='device_add'),
            url(r'^device/(?P<serial>[^/]+)/$', \
                    user.DeviceDetail.as_view(), name='device_item'),
            url(r'^device/(?P<serial>[^/]+)/delete/$', \
                    admin.DeviceDelete.as_view(), name='device_delete'),
            url(r'^device/(?P<serial>[^/]+)/edit/$', \
                    admin.DeviceEdit.as_view(), name='device_edit'),
            url(r'^device/(?P<serial>[^/]+)/note/$', \
                    user.NoteList.as_view(), name='note_list'),
            url(r'^device/(?P<serial>[^/]+)/note/add/$', \
                    admin.NoteCreate.as_view(), name='note_add'),
            url(r'^device/(?P<serial>[^/]+)/note/(?P<note_id>\d+)/$', \
                    user.NoteDetail.as_view(), name='note_item'),
            url(r'^device/(?P<serial>[^/]+)/note/(?P<note_id>\d+)/delete/$', \
                    admin.NoteDelete.as_view(), name='note_delete'),
            url(r'^device/(?P<serial>[^/]+)/note/(?P<note_id>\d+)/edit/$', \
                    admin.NoteEdit.as_view(), name='note_edit'),
            url(r'^device/(?P<serial>[^/]+)/status/$', \
                    admin.StatusCreate.as_view(), name='status_create'),
            url(r'^device/(?P<serial>[^/]+)/return/$', \
                    admin.StatusUpdate.as_view(), name='status_edit'),
            )
