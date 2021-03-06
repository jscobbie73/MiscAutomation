from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler
from getpass import getpass

import sys

host=sys.argv[1]
free_num = 0
gam_cfg = CiscoConfParse(gamconfig)

password = getpass()

gam = {
	'device_type': 'cisco_ios',
	'ip': host,
	'username': 'starry',
	'password': password,
	} 

net_connect = ConnectHandler(**gam)
output = net_connect.send_command("show interface")
gam_cfg = CiscoConfParse(output)

free_ports = gam_cfg.find_objects_wo_child(parentspec=r"^Interface g", childspec=r"customer/")
#hostname = gam_cfg.find_objects(r"^hostname")[0].text[9:]



for my_int in free_ports:
	free_num = free_num + 1

print(host)
print("Free Ports:")
print(free_num)

