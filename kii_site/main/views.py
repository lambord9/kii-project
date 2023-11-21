from django.shortcuts import render, redirect, HttpResponse
from .models import Device

dev1 = Device('Fortigate', 'FG-1500D', 'Fortigate-01', 'serial111', 'Active', 'г. Новосибирск, ул. Ленина, д.1', 'Узел ИБ', 'https://10.1.1.1')
dev2 = Device('Fortigate', 'FG-600E', 'Fortigate-02', 'serial222', 'Active', 'г. Тюмень, пр. Мира, д.2', 'Площадка', 'https://10.2.2.1')
dev3 = Device('Континент', 'IPC-3000NF2', 'АПК-01', '№2354565', 'Passive', 'г. Магадан, ул. Пионерская, д.3', 'Площадка', 'https://10.3.3.1')
all_devices = [dev1, dev2, dev3]

def index(request):
    context = {'title': 'Портал КИИ - Главная страница'}
    return render(request, 'main/index.html', context)

def profile(request):
    return render(request, 'main/profile.html')

def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контакты'})

def template(request):
    return render(request, 'main/base_template.html')

def devices(request):
    
    context = {'title': 'Портал КИИ - Устройства', 'all_devices': all_devices}
    return render(request, 'main/devices.html', context)

def get_device(request, id):
    context = {'title': 'Портал КИИ - Подробнее об устройстве', 'device': all_devices[id-1], 'id': id}
    return render(request, 'main/device_single.html', context)

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')

def profile(request):
    return render(request, 'main/profile.html')

#def custom_404(request, exception):
#    return render(request, 'main/custom_404.html')
def custom_404(request, exception):
    return HttpResponse('ОЙ')


