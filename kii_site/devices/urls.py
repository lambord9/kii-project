from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'devices_index'),
    path('<int:pk>', views.DeviceDetailView.as_view(), name = 'device_single'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
