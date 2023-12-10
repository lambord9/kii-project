from django.shortcuts import render, get_object_or_404
from .models import *


def index(request): 
    all_devices = Device.objects.all()
    context = {'title': 'Портал КИИ - Устройства', 'all_devices': all_devices}
    return render(request, 'devices/devices.html', context)

def get_device(request, id:int):
    device = get_object_or_404(Device, id=id)
    context = {
        'title': 'Портал КИИ - Подробнее об устройстве', 
        'device': device,        
        }
    return render(request, 'devices/device_single.html', context)