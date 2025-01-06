from netmiko import ConnectHandler
from cmdb_app.models import NetworkEquipment


class Network:

    def device_connexion(self, *args, **kwargs):
        for equipment in NetworkEquipment.objects.all():

            device = {
                "device_type": equipment.device_type,
                "host": equipment.host,
                "username": equipment.username,
                "password": equipment.password,
                "port": equipment.port,
            }

            net_connect = ConnectHandler(**device)
            # Vérification de l'uptime
            version_output = net_connect.send_command("show version")
            if "uptime is" in version_output:
                uptime = version_output.split("uptime is")[1].split(",")[0]
                print(f"Le routeur est actif depuis : {uptime}")
            else:
                print("Impossible de déterminer l'uptime")
            print(version_output)
