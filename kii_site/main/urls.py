from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('profile/', views.profile, name = 'profile'),
    path('contacts/', views.contacts, name = 'contacts'),
    path('template/', views.template, name = 'template'),
    path('devices/', views.devices, name = 'devices'),
    path('devices/<int:id>', views.get_device, name = 'device_single'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login, name = 'login'),
    path('profile/', views.profile, name = 'profile'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
