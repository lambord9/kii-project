from django.db import models

class Device:
    counter = 0
    def __init__(self, type, model, name, serial, status, address, sitetype, ip):
        Device.counter +=1
        self.type = type
        self.model = model
        self.name = name
        self.serial = serial
        self.status = status
        self.address = address
        self.sitetype = sitetype
        self.ip = ip
 