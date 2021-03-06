from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.encoding import smart_unicode

from meraki_inv.models import Device, Note, Status

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        exclude = ['device', 'edited']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        exclude = ['device', 'loaner', 'returned']
