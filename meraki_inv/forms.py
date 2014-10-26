from django import forms
from django.core.exceptions import ValidationError

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
        exclude = ['device', 'returned']
