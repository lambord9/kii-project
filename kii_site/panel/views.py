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
        context["qs"] = {
            'device_count_by_domain': Domain.objects.annotate(Count('device')),
            'device_count_by_domain_sz' : Domain.objects.filter(device__address__mrf='SZ').annotate(Count('device')),
            'device_count_by_domain_dv' : Domain.objects.filter(device__address__mrf='DV').annotate(Count('device')),
            'device_count_by_domain_vl' : Domain.objects.filter(device__address__mrf='VL').annotate(Count('device')),
            'device_count_by_domain_si' : Domain.objects.filter(device__address__mrf='SI').annotate(Count('device')),
            'device_count_by_domain_ug' : Domain.objects.filter(device__address__mrf='UG').annotate(Count('device')),
            'device_count_by_domain_ur' : Domain.objects.filter(device__address__mrf='UR').annotate(Count('device')),
            'device_count_by_domain_cn' : Domain.objects.filter(device__address__mrf='CN').annotate(Count('device')),
        }
        print(context)
        return context
    
    
# class DomainsByMRFChartView(TemplateView):
#     template_name = 'panel/panel.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["qs"] = Domain.objects.annotate(Count('device', filter=Q(Address.MRF_CHOISES == 'SI')))
#         return context
    