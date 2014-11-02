from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
import datetime

from meraki_inv.forms import DeviceForm, NoteForm, StatusForm
from meraki_inv.models import Device, Note, Status
from meraki_inv.views import user

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class DeviceCreate(LoginRequiredMixin, generic.CreateView):
    form_class = DeviceForm
    model = Device

class DeviceDelete(LoginRequiredMixin, generic.DeleteView):
    model = Device
    pk_url_kwarg = "serial"
    success_url = reverse_lazy('meraki_inv:device_list')

class DeviceEdit(LoginRequiredMixin, generic.UpdateView):
    model = Device
    form_class = DeviceForm
    pk_url_kwarg = "serial"
    template_name_suffix = '_update_form'

class NoteCreate(LoginRequiredMixin, generic.CreateView):
    model = Note
    form_class = NoteForm

    def form_valid(self, form):
        form.instance.device_id = self.kwargs.get('serial')
        return super(NoteCreate, self).form_valid(form)

class NoteDelete(LoginRequiredMixin, generic.DeleteView):
    model = Note
    pk_url_kwarg = "note_id"

    def get_object(self, queryset=None):
            if queryset is None:
                queryset = self.get_queryset()
            device = self.kwargs['serial']
            note = self.kwargs['note_id']
            context = {'note_id':note, 'serial':device}
            return context

    def delete(self, request, *args, **kwargs):
        device = self.kwargs['serial']
        note = self.kwargs['note_id']

        note_obj = Note.objects.filter(device=device, id=note)
        note_obj.delete()
        return HttpResponseRedirect(reverse('meraki_inv:note_list', \
            kwargs={'serial': device}))

class NoteEdit(LoginRequiredMixin, generic.UpdateView):
    model = Note
    form_class = NoteForm
    pk_url_kwarg = "note_id"
    template_name_suffix = '_update_form'

class StatusCreate(LoginRequiredMixin, generic.CreateView):
    model = Status
    form_class = StatusForm
    pk_url_kwarg = "serial"

    def form_valid(self, form):
        form.instance.device_id = self.kwargs.get('serial')
        return super(StatusCreate, self).form_valid(form)

class StatusUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Status
    form_class = StatusForm
    pk_url_kwarg = "serial"

    def post(self, request, *args, **kwargs):
        device = self.kwargs['serial']
        status = Status.objects.filter(device=device).latest()
        status.returned = datetime.datetime.now()
        status.save()
        return HttpResponseRedirect(reverse('meraki_inv:device_item', \
            kwargs={'serial': device}))
