from django import forms
from .models import Device
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['dev_type', 'model', 'hostname', 'status', 'mgmt_inband_ip', 'mgmt_loopback_ip', 'domains']
        widgets = {'dev_type': Select(),
                   'model': Textarea(attrs={'cols':30, 'rows':1}),
                   'hostname': Textarea(attrs={'cols':30, 'rows':1}),
                   'status': Select(),
                   'mgmt_inband_ip': Textarea(attrs={'cols':30, 'rows':1}),
                   'mgmt_loopback_ip': Textarea(attrs={'cols':30, 'rows':1}),
                   'domains': CheckboxSelectMultiple(),
        }
