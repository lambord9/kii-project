from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    context = {'title': 'Портал КИИ - Главная страница'}
    return render(request, 'main/index.html', context)

def profile(request):
    return render(request, 'main/profile.html')

def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контакты'})

def template(request):
    return render(request, 'main/base_template.html')

def register(request):
    return render(request, 'main/register.html')

def login(request):
    return render(request, 'main/login.html')

def profile(request):
    return render(request, 'main/profile.html')

def custom_404(request, exception):
    return render(request, 'all_apps/404.html', status=404)


