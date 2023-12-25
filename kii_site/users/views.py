from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group

@login_required(login_url='/users/login')
def feedback(request):
    if not request.user.is_authenticated:
        return redirect('users/login.html')
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data)
        else:
            print('Ошибка, сообщение не отправлено', form.errors)
    form = FeedbackForm()
    context = {'form': form}
    return render(request, 'users/feedback.html', context=context)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name="Read/Write")
            user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            authenticate(username=username, password=password)
            messages.success(request, f"{username} зарегистрирован")
            return redirect('home')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    context = {'form': form}
    return render(request, 'users/register.html', context=context)

@login_required(login_url='/users/login')
def profile(request):
    if not request.user.is_authenticated:
        return redirect('users/login.html')
    return render (request, 'users/profile.html')

class UserLogoutView(LoginRequiredMixin, LogoutView):
    def get_success_url(self):
        return self.request.META['HTTP_REFERER']