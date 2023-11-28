from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['hostname', 'dev_type', 'model', 'status', 'address','mgmt_inband_ip', 'mgmt_loopback_ip', 'ups']
    list_editable = ['dev_type', 'model', 'status', 'address', 'mgmt_inband_ip', 'mgmt_loopback_ip']
    ordering = ['hostname']

    list_per_page = 30
    list_filter = ['hostname', 'model', 'status', 'ups']


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['node', 'serial', 'support_date', 'mgmt_ooband_ip']
    list_editable = ['serial', 'support_date', 'mgmt_ooband_ip']
    ordering = ['node']
    list_per_page = 30

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address','mrf', 'territory_type', 'contacts']
    ordering = ['address']
    list_per_page = 30
    list_filter = ['address', 'mrf', 'territory_type']








