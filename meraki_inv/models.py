from django import forms
from django.core.urlresolvers import reverse
from django.db import models

import datetime

# Create your models here.
class Device(models.Model):
    access = models.CharField(max_length=45)
    accessories = models.CharField(max_length=45, blank=True)
    features = models.CharField(max_length=45, blank=True)
    make = models.CharField(max_length=45)
    model = models.CharField(max_length=45)
    model_num = models.CharField("model_num", max_length=45, blank=True)
    pword = models.CharField(max_length=45,blank=True)
    serial = models.CharField("serial", max_length=45)
    uname = models.CharField("uname", max_length=45, blank=True)
    def loaned(self):
        loaned = Status.objects.filter(device=self.id).latest()
        return loaned
    def __unicode__(self):
        return self.model
    def get_absolute_url(self):
        return reverse('meraki_inv:device_item', args=(self.pk,))

class Status(models.Model):
    device = models.ForeignKey('Device')
    loaned = models.DateTimeField('Date Loaned', auto_now=True, editable=False)
    loaner = models.CharField(max_length=45)
    mooch = models.CharField(max_length=45)
    returned = models.DateTimeField('Date Returned', null=True)
    def get_absolute_url(self):
        return reverse('meraki_inv:device_item', args=(self.device.id,))
    class Meta:
        get_latest_by = "loaned"

class Note(models.Model):
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=200)
    device = models.ForeignKey('Device')
    submitted = models.DateField('Submitted', auto_now=True, editable=False)
    edited = models.DateField('Edited', auto_now=True, editable=False)
    def get_absolute_url(self):
        return reverse('meraki_inv:device_item', args=(self.device.id,))
