from django import forms
from .models import Device
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, Select

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        fields = ['dev_type', 'model', 'hostname', 'status', 'mgmt_inband_ip', 'mgmt_loopback_ip', 'domains']
        widgets = {'dev_type': Select(attrs={'style':'max-width:25vh'}),
                   'model': Textarea(attrs={'cols':5, 'rows':1, 'style':'max-width:25vh'}),
                   'hostname': Textarea(attrs={'cols':5, 'rows':1, 'style':'max-width:25vh'}),
                   'status': Select(attrs={'style':'max-width:25vh'}),
                   'mgmt_inband_ip': Textarea(attrs={'cols':5, 'rows':1, 'style':'max-width:25vh'}),
                   'mgmt_loopback_ip': Textarea(attrs={'cols':5, 'rows':1, 'style':'max-width:25vh'}),
                   'domains': CheckboxSelectMultiple(attrs={'style':'max-width:25vh'}),
        }

