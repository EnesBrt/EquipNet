from netmiko import ConnectHandler
from cmdb_app.models import NetworkEquipment


class Network:
    """
    Collect equipment data from the database and connect to check if the equipments are active or not.
    """

    def device_connection(self, *args, **kwargs):
        # Retrieve all the equipments from the database
        for equipment in NetworkEquipment.objects.all():
            device = {
                "device_type": equipment.device_type,
                "host": equipment.host,
                "username": equipment.username,
                "password": equipment.password,
                "port": equipment.port,
            }

            # Equipment connection
            net_connect = ConnectHandler(**device)

            # Check if equipment is active or not
            version_output = net_connect.send_command("show version")
            if "uptime is" in version_output:
                equipment.status = "Actif"
            else:
                equipment.status = "Inactif"
            equipment.save()
