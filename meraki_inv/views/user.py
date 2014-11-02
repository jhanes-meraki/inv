from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
import datetime

from meraki_inv.forms import DeviceForm, NoteForm, StatusForm
from meraki_inv.models import Device, Note, Status

class DeviceDetail(generic.DetailView):
    model = Device
    pk_url_kwarg = "serial"

    def get_context_data(self, **kwargs):
        context = super(DeviceDetail, self).get_context_data(**kwargs)
        context['status'] = Status.objects.filter(
                device=self.kwargs['serial'])
        context['notes'] = Note.objects.filter(device=self.kwargs['serial'])
        return context

class DeviceList(generic.ListView):
    model = Device

    def get_queryset(self):
        query = self.request.REQUEST.get("search_query")
        if not query:
            device_list = self.model.objects.all()
        else:
            q = Q(access__icontains=query) | Q(make__icontains=query) | \
                    Q(model__icontains=query) | \
                    Q(model_num__icontains=query) | \
                    Q(serial__icontains=query) 
            #TODO Additional query options
            #q = Q(access__icontains=query) | Q(accessories__icontains=query) | \
            #        Q(features__icontains=query) | Q(make__icontains=query) | \
            #        Q(model__icontains=query) | \
            #        Q(model_num__icontains=query) | \
            #        Q(pword__icontains=query) | Q(serial__icontains=query) | \
            #        Q(uname__icontains=query)
            device_list = self.model.objects.filter(q)
        return device_list

class NoteDetail(generic.DetailView):
    model = Note
    pk_url_kwarg = "note_id"

    def get_context_data(self, **kwargs):
        context = super(NoteDetail, self).get_context_data(**kwargs)
        return context

class NoteList(generic.ListView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteList, self).get_context_data(**kwargs)
        context['device'] = Device.objects.get(pk=self.kwargs['serial'])
        context['notes'] = Note.objects.filter(device=self.kwargs['serial'])
        return context
