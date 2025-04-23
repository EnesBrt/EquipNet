from django.db import models


class Equipments(models.Model):
    device_name = models.CharField(max_length=255, blank=True)
    device_type = models.CharField(max_length=255)
    host = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    port = models.IntegerField(default=50, blank=True)
    secret = models.CharField(max_length=255, blank=True)
    
    
    STATUS = [
        ("connected", "Connected"),
        ("disconnected", "Disconnected"),
    ]
    
    status = models.CharField(max_length=255, choices=STATUS, default="Disconnected")
    
    
    def __str__(self):
        return self.device_name
    
    
    
    
    