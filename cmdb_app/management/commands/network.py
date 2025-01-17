from netmiko import ConnectHandler
from cmdb_app.models import NetworkEquipment
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        for equipment in NetworkEquipment.objects.all():
            device = {
                "device_type": equipment.device_type,
                "host": equipment.host,
                "username": equipment.username,
                "password": equipment.password,
                "port": equipment.port,
            }

            net_connect = ConnectHandler(**device)

            version_output = net_connect.send_command("show version")
            if "uptime is" in version_output:
                equipment.status = "Active"
            else:
                equipment.status = "Inactive"
            equipment.save()

        print("The program is running...")
