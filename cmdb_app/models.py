from django.db import models
from django.contrib.auth.models import User


class NetworkEquipment(models.Model):
    """
    Represents a piece of network equipment with basic information and status.
    """

    # Basic information about the equipment
    from django.db import models


from django.contrib.auth.models import User


class NetworkEquipment(models.Model):
    """
    Represents a piece of network equipment with basic information and status.
    """

    # Basic information about the equipment
    device_name = models.CharField(max_length=100, unique=True)
    device_type = models.CharField(max_length=50)
    ip_address = models.CharField(unique=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    port = models.IntegerField(null=True, blank=True)

    # Status of the equipment
    STATUS_CHOICES = [
        ("actif", "Actif"),
        ("inactif", "Inactif"),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="inactif",
    )

    # Timestamp for when the equipment was added or last updated
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the model."""
        return self.device_name
