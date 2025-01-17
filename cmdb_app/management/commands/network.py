from netmiko import ConnectHandler
from cmdb_app.models import NetworkEquipment
from django.core.management.base import BaseCommand
import signal
import time
import sys


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        help = "Runs a command to check network equipment status indefinitely"

        def signal_handler(sig, frame):
            self.stdout.write(self.style.SUCCESS("Exiting gracefully"))
            sys.exit(0)

            signal.signal(signal.SIGINT, signal_handler)

            self.stdout.write("Press Ctrl+C to stop the program")

            while True:

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

                self.stdout.write("Program is running...")
                time.sleep(60)
