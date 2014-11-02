#"""
#admin view
#"""
#from django.contrib import admin
#from meraki_inv.models import Device, Status
#
#class DeviceAdmin(admin.ModelAdmin):
#    """
#    view for devices in admin
#    """
#    fields = ['make', 'model', 'model_num', 'serial', 'access', 'accessories',\
#            'features', 'uname', 'pword']
#    list_display = ('model', 'make', 'model_num', 'serial', 'access', 'loaned')
#
#class StatusAdmin(admin.ModelAdmin):
#    """
#    view for status' in admin
#    """
#    fields = ['device', 'loaned', 'mooch', 'loaner', 'returned']
#
#admin.site.register(Device, DeviceAdmin)
#admin.site.register(Status, StatusAdmin)
