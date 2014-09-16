from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
import datetime

from meraki_inv.forms import DeviceForm, NoteForm, StatusForm
from meraki_inv.models import Device, Note, Status

class DeviceCreate(generic.CreateView):
    model = Device
    form_class = DeviceForm

class DeviceDelete(generic.DeleteView):
    model = Device
    pk_url_kwarg = "device_id"
    success_url = reverse_lazy('meraki_inv:device_list')

class DeviceDetail(generic.DetailView):
    model = Device
    pk_url_kwarg = "device_id"

    def get_context_data(self, **kwargs):
        context = super(DeviceDetail, self).get_context_data(**kwargs)
        context['status'] = Status.objects.filter(
                device=self.kwargs['device_id'])
        context['notes'] = Note.objects.filter(device=self.kwargs['device_id'])
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

class DeviceEdit(generic.UpdateView):
    model = Device
    form_class = DeviceForm
    pk_url_kwarg = "device_id"
    template_name_suffix = '_update_form'

class NoteAdd(generic.CreateView):
    model = Note
    form_class = NoteForm

class NoteDelete(generic.DeleteView):
    model = Note
    pk_url_kwarg = "note_id"

    def get_object(self, queryset=None):
            if queryset is None:
                queryset = self.get_queryset()
            device = self.kwargs['device_id']
            note = self.kwargs['note_id']
            context = {'note_id':note, 'device_id':device}
            return context

    def delete(self, request, *args, **kwargs):
        device = self.kwargs['device_id']
        note = self.kwargs['note_id']

        note_obj = Note.objects.filter(device=device, id=note)
        note_obj.delete()

class NoteDetail(generic.DetailView):
    model = Note
    pk_url_kwarg = "note_id"

    def get_context_data(self, **kwargs):
        context = super(NoteDetail, self).get_context_data(**kwargs)
        return context

class NoteEdit(generic.UpdateView):
    model = Note
    form_class = NoteForm
    pk_url_kwarg = "note_id"
    template_name_suffix = '_update_form'

class NoteList(generic.ListView):
    model = Note

    def get_context_data(self, **kwargs):
        context = super(NoteList, self).get_context_data(**kwargs)
        context['device'] = Device.objects.get(pk=self.kwargs['device_id'])
        context['notes'] = Note.objects.filter(device=self.kwargs['device_id'])
        return context

class StatusCreate(generic.CreateView):
    model = Status
    form_class = StatusForm
    pk_url_kwarg = "device_id"

#   if request.GET:
#       initial = request.GET.copy()
#       print initial


class StatusUpdate(generic.UpdateView):
    model = Status
    form_class = StatusForm
    pk_url_kwarg = "device_id"

    def post(self, request, *args, **kwargs):
        device = self.kwargs['device_id']
        status = Status.objects.filter(device=device).latest()
        status.returned = datetime.datetime.now()
        status.save()
        return HttpResponseRedirect(reverse('meraki_inv:device_item', \
            kwargs={'device_id': device}))
