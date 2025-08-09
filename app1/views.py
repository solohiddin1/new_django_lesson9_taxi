from django.shortcuts import render
from .models import *
from django.views.generic import ListView, CreateView , UpdateView , DeleteView, DetailView 
from .forms import ClientForm,DriverForm,TarifForm,DealForm,CommentForm
from django.urls import reverse_lazy

# Create your views here.


def home(request):
    deals = Deal.objects.all()
    context = {
        'deals':deals
    }
    return render(request,'index.html',context=context)

def manage_users(request):
    clients = Client.objects.all()
    drivers = Driver.objects.all()
    admins = Admin.objects.all()
    deals = Deal.objects.all()

    return render(request, 'admin_dashboard.html', {
        'clients': clients,
        'drivers': drivers,
        'admins': admins,
        'deals':deals
    })


class ClientListView(ListView):
    model = Client
    template_name = 'client_dashboard.html'
    context_object_name = 'client'

class DriverListView(ListView):
    model = Driver
    template_name = 'driver_dashboard.html'
    context_object_name = 'driver'


# class AdminListView(ListView):
#     model = Admin
#     template_name = 'admin_dashboard.html'
#     context_object_name = 'admin'


class AddClientView(CreateView):
    form_class = ClientForm
    template_name = 'add_client.html'
    success_url = reverse_lazy('admin_panel')


class AddDriverView(CreateView):
    form_class = DriverForm
    template_name = 'add_driver.html'
    success_url = reverse_lazy('admin_panel')


class AddDealView(CreateView):
    form_class = DealForm
    template_name = 'add_deal.html'
    success_url = reverse_lazy('client')


class AddTarifView(CreateView):
    form_class = TarifForm
    template_name = 'add_tarif.html'
    success_url = reverse_lazy('admin_panel')


class UpdateDriver(UpdateView):
    model = Driver
    form_class = DriverForm
    template_name = 'update_driver.html'
    success_url = reverse_lazy('admin_panel')


class UpdateClient(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'update_client.html'
    success_url = reverse_lazy('admin_panel')


class DeleteDriver(DeleteView):
    model = Driver
    template_name = 'delete_driver.html'
    success_url = reverse_lazy('admin_panel')


class DeleteClient(DeleteView):
    model = Client
    template_name = 'delete_client.html'
    success_url = reverse_lazy('admin_panel')


class UpdateDeal(UpdateView):
    model = Deal
    form_class = DealForm
    template_name = 'update_deal.html'
    success_url = reverse_lazy('admin_panel')


class DeleteDeal(DeleteView):
    model = Deal
    template_name = 'delete_dela.html'
    success_url = reverse_lazy('admin_panel')

