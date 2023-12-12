from typing import Any
from django.shortcuts import render, HttpResponse
from devices.models import *
from django.db.models import Count, Q
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class DomainsChartView(LoginRequiredMixin, TemplateView):
    login_url='/users/login'
    template_name = 'panel/panel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Domain.objects.annotate(Count('device'))
        return context
    
class DomainsByMRFChartView(TemplateView):
    template_name = 'panel/panel.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Domain.objects.annotate(Count('device', filter=Q(Address.MRF_CHOISES == 'SI')))
        return context