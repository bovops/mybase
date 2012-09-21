# Create your views here.
from models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404

class ClientList(ListView):
    model = Client
    context_object_name = 'clients'
    paginate_by = 20
    queryset = Client.objects.order_by('name')

class ClientDetail(DetailView):
    model = Client
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super(ClientDetail, self).get_context_data(**kwargs)
#        context['servers'] =
#        context['pays'] =
#        context['tickets'] =
        return context