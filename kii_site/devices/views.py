from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='/users/login')
def index(request): 
    form = DeviceForm(request.POST)
    if not request.user.is_authenticated:
        return redirect('users/login.html')
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('devices_index')
    all_devices = Device.objects.all()
    context = {'title': 'Портал КИИ - Устройства', 'all_devices': all_devices, 'form': form}
    return render(request, 'devices/devices.html', context)


class DeviceDetailView(LoginRequiredMixin, DetailView):
    login_url='/users/login'
    model = Device
    template_name = 'devices/device_single.html'
    context_object_name = 'device'

# def create_device(request):
    
#     return render(request, 'devices/devices.html', {'form': form})