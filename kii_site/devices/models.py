from django.db import models
from django.urls import reverse

#from devices.models import Device
#  

class Device(models.Model):
    active = 'A'
    non_active = 'N'
    prod = 'P'

    STATUS_CHOISES = [
        (active, 'Active'),
        (non_active, 'Non-active'),
        (prod, 'Prod'),
    ]

    DEV_TYPE_CHOISES = [
        ('FG', 'FortiGate'),
        ('FSW', 'FortiSWitch'),
        ('FAU', 'FortiAuthenticator'),
        ('FAZ', 'FortiAnalyzer'),
        ('FMG', 'FortiManager'),
        ('NG', 'NGate'),
        ('TS', 'TufinServer'),
        ('TC', 'TufinCollector'),
        ('К', 'Континент'),
        ('КЦ', 'Континент (ЦУС)'),
    ]

    dev_type = models.CharField(max_length=5, choices=DEV_TYPE_CHOISES, null=True)
    model = models.CharField(max_length=10, null=True, blank=True)
    hostname = models.CharField(max_length=15)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES)
    mgmt_inband_ip = models.CharField(max_length=25, null=True)
    mgmt_loopback_ip = models.CharField(max_length=25, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    firmware = models.ForeignKey('Firmware', on_delete=models.CASCADE, null=True, blank=True)
    domains = models.ManyToManyField('Domain')

    def get_url(self):
        return reverse('device_single', args=[self.id])
    
    def get_model_fields(self):
        return self._meta.fields

    def __str__(self):
        return f'{self.id}- {self.hostname}'
    
class Node(models.Model):

    hostname = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    node = models.CharField(max_length=15)
    serial = models.CharField(max_length=30)
    support_date = models.DateField()
    mgmt_ooband_ip = models.CharField(max_length=25, null=True)
    ups = models.CharField(max_length=200, default='Имеется')

class Address(models.Model):
    SZ = 'SZ'
    DV = 'DV'
    VL = 'VL'
    SI = 'SI'
    UG = 'UG'
    UR = 'UR'
    CN = 'CN'
    
    MRF_CHOISES = [
        (SZ, 'Северо-запад'),
        (DV, 'Дальний восток'),
        (VL, 'Волга'),
        (SI, 'Сибирь'),
        (UG, 'Юг'),
        (UR, 'Урал'),
        (CN, 'Центр'),
    ]
    mrf = models.CharField(max_length=2, choices=MRF_CHOISES, null=True, blank=True)
    address = models.CharField(max_length=200, default=None)
    territory_type = models.CharField(max_length=20, null=True)
    contacts = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.address}'
    

class Domain(models.Model):

    domain = models.CharField(max_length=7, default=None, null=True)

    def __str__(self):
        return f'{self.domain}'

class Firmware(models.Model):

    firmware = models.CharField(max_length=15, default='6.4.13')
    build = models.CharField(max_length=15, default='2060')

    def __str__(self):
        return f'{self.firmware} build{self.build}'



    


