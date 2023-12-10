from typing import Any
from django.shortcuts import render, HttpResponse
from devices.models import *
from django.db.models import Count
from django.views.generic import TemplateView


# def index(request): 
#     count_domains = Domain.objects.annotate(Count('device'))
#     print(count_domains)
#     domains = {}
#     for d in count_domains:
#         domains[d]= d.device__count

#     context = {'title': 'Портал КИИ - Панель управления', 'domains': domains}
#     print(context)
#     return render(request, 'panel/panel.html', context)

class DomainsChartView(TemplateView):
    template_name = 'panel/panel.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = Domain.objects.annotate(Count('device'))
        return context