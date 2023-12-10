from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views
from panel.views import DomainsChartView

urlpatterns = [
    path('', DomainsChartView.as_view(), name = 'panel_index'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
