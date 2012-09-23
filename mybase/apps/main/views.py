# -*- coding: utf8 -*-

# Create your views here.
from models import *
from django.views.generic import ListView, DetailView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404

class ClientMixin(object):
    model = Client

class ClientList(ClientMixin, ListView):
    context_object_name = 'clients'
    paginate_by = 20
    queryset = Client.objects.order_by('name')


class ClientDetail(ClientMixin, DetailView):
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super(ClientDetail, self).get_context_data(**kwargs)
#        context['servers'] =
#        context['pays'] =
#        context['tickets'] =
        return context


class ClientDelete(ClientMixin, DeleteView):
    success_url = '/clients'

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Клиент удален')
        return super(ClientDelete, self).delete(request, *args, **kwargs)
