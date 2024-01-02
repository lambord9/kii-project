from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib import messages


def check_group(*groups):
    def decorator(function):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if user.groups.filer(name__in=groups).exists():
                return function(request,*args,**kwargs)
            messages.warning(request,'Нет доступа')
            return (HttpResponseRedirect(request.POST.get('next','/')))
        return wrapper
    return decorator