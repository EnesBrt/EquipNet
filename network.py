from netmiko import ConnectHandler

# Just pick an 'invalid' device_type
cisco = {
    "device_type": "cisco_xe",
    "host": "devnetsandboxiosxe.cisco.com",
    "username": "admin",
    "password": "C1sco12345",
    "port": 22,
}

net_connect = ConnectHandler(**cisco)
# Vérification de l'uptime
version_output = net_connect.send_command("show version")
if "uptime is" in version_output:
    uptime = version_output.split("uptime is")[1].split(",")[0]
    print(f"Le routeur est actif depuis : {uptime}")
else:
    print("Impossible de déterminer l'uptime")
print(version_output)
