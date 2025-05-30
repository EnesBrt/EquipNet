from django.contrib import admin
from .models import Equipments


class EquipmentsAdmin(admin.ModelAdmin):
    list_display = (
        "device_name",
        "device_type",
        "host",
        "username",
        "password",
        "port",
        "secret",
        "status",
    )


admin.site.register(Equipments, EquipmentsAdmin)
