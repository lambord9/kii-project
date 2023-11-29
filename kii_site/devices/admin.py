from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['hostname',  'dev_type', 'model', 'firmware', 'status', 'address','mgmt_inband_ip', 'mgmt_loopback_ip']
    list_editable = ['dev_type', 'model', 'status', 'firmware', 'address', 'mgmt_inband_ip', 'mgmt_loopback_ip']
    ordering = ['hostname']
    #filter_horizontal = ['domains']
    list_per_page = 30
    list_filter = ['hostname', 'status', 'firmware']


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ['node',  'serial', 'support_date', 'mgmt_ooband_ip', 'ups']
    list_editable = [ 'serial', 'support_date', 'mgmt_ooband_ip', 'ups']
    ordering = ['node']
    list_per_page = 30

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['address','mrf', 'territory_type', 'contacts']
    ordering = ['address']
    list_per_page = 30
    list_filter = ['address', 'mrf', 'territory_type']

@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['domain']
    list_filter = ['domain']

@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    list_display = ['firmware', 'build']
    list_filter = ['firmware', 'build']










