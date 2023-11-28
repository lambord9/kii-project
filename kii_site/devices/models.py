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
        ('F', 'Fortigate'),
        ('К', 'Континент'),
        ('T', 'Tufin'),
    ]


    hostname = models.CharField(max_length=15)
    dev_type = models.CharField(max_length=20, choices=DEV_TYPE_CHOISES)
    model = models.CharField(max_length=15)
    status = models.CharField(max_length=1, choices=STATUS_CHOISES)
    address = models.ForeignKey('Address', on_delete=models.CASCADE, null=True)
    mgmt_inband_ip = models.CharField(max_length=25, null=True)
    mgmt_loopback_ip = models.CharField(max_length=25, null=True)
    ups = models.CharField(max_length=200, default='Имеется')

    def get_url(self):
        return reverse('device_single', args=[self.id])
    
    def get_model_fields(self):
        return self._meta.fields

    def __str__(self):
        return f'{self.id}- {self.hostname}'
    
class Node(models.Model):
    hostname = models.ForeignKey(Device, on_delete=models.CASCADE, null=True)
    node = models.CharField(max_length=15)
    firmware = models.CharField(max_length=15, default='6.4')
    serial = models.CharField(max_length=30)
    support_date = models.DateField()
    mgmt_ooband_ip = models.CharField(max_length=25, null=True)

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
        return f'{self.address} - {self.territory_type}'




    


