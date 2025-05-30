from typing import Any
from netmiko import ConnectHandler
from django.core.management.base import BaseCommand
from equipments.models import Equipments


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument(
            "--connect", action="store_true", help="connect to the device"
        )

        parser.add_argument(
            "--disconnect", action="store_true", help="disconnect from the device"
        )

    def handle(self, *args, **options):
        equipments = Equipments.objects.all()

        for equimpent in equipments:

            device = {
                "device_type": equimpent.device_type,
                "host": equimpent.host,
                "username": equimpent.username,
                "password": equimpent.password,
                "port": equimpent.port,
                "secret": equimpent.secret,
            }
            connection = ConnectHandler(**device)

            if options["connect"]:
                if connection.is_alive():
                    equimpent.status = "connected"
                    equimpent.save()
                    self.stdout.write(
                        self.style.SUCCESS("Successfully connected to the device")
                    )

            if options["disconnect"]:
                connection.disconnect()
                equimpent.status = "disconnected"
                equimpent.save()
                self.stdout.write(
                    self.style.SUCCESS("Successfully disconnected from the device")
                )

            if not options["connect"] and not options["disconnect"]:
                self.stdout.write(
                    self.style.WARNING("Please specify --connect or --disconnect")
                )


"""
device = {
    'device_type': 'cisco_xe',
    'host':   'devnetsandboxiosxe.cisco.com',
    'username': 'admin',
    'password': 'C1sco12345',
    'port' : 22,          # optional, defaults to 22
    'secret': '',     # optional, defaults to ''
}

connection = ConnectHandler(**device)

print(connection.send_command("show ip interface brief"))

if connection.is_alive():
    print("The device is running")
else:
    print("The device is not running")

connection.disconnect()

"""
