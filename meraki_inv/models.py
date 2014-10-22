from django import forms
from django.core.urlresolvers import reverse
from django.db import models

import datetime

# Create your models here.
class Device(models.Model):
    access = models.CharField('Access', max_length=45)
    accessories = models.CharField('Accessories', max_length=45, blank=True)
    features = models.CharField('Features', max_length=45, blank=True)
    make = models.CharField('Make', max_length=45)
    model = models.CharField('Model', max_length=45)
    model_num = models.CharField('Model Number', max_length=45, blank=True)
    pword = models.CharField('Password', max_length=45,blank=True)
    serial = models.CharField('Serial', primary_key=True, max_length=45)
    uname = models.CharField('Username', max_length=45, blank=True)
    def loaned(self):
        loaned = Status.objects.filter(device=self.serial).latest()
        return loaned
    def __unicode__(self):
        return self.serial
    def get_absolute_url(self):
        return reverse('meraki_inv:device_item', args=(self.serial,))

class Status(models.Model):
    device = models.ForeignKey('Device')
    loaned = models.DateTimeField('Date Loaned', auto_now_add=True, \
            editable=False)
    loaner = models.CharField('Loaner', max_length=45)
    mooch = models.CharField('Mooch', max_length=45)
    returned = models.DateTimeField('Date Returned', null=True)
    def get_absolute_url(self):
        return reverse('meraki_inv:device_item', args=(self.device.serial,))
    class Meta:
        get_latest_by = "loaned"

class Note(models.Model):
    name = models.CharField(max_length=45)
    desc = models.CharField(max_length=200)
    device = models.ForeignKey('Device')
    submitted = models.DateField('Submitted', auto_now=True, editable=False)
    edited = models.DateField('Edited', auto_now=True, editable=False)
    def get_absolute_url(self):
        return reverse('meraki_inv:device_item', args=(self.device.serial,))
