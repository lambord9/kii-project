from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required

@login_required(login_url='/users/login')
def index(request):
    if not request.user.is_authenticated:
        return redirect('users/login.html')
    context = {'title': 'Портал КИИ - Главная страница'}
    return render(request, 'main/index.html', context)

def profile(request):
    return render(request, 'main/profile.html')

def custom_404(request, exception):
    return render(request, 'all_apps/404.html', status=404)


