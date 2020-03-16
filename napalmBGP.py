import json
from napalm import get_network_driver
driver = get_network_driver('ios')

deviceIP = ['192.168.122.253', '192.168.122.254']

for ip in deviceIP:
    print('Connecting ' + ip)
    ios = driver(ip,'celestine','cisco')

    ios.open() # opens my connection to the device

    ios_output = ios.get_bgp_neighbors()
    print (json.dumps(ios_output,indent = 4))
    ios_output = ios.get_interfaces_ip()
    print(json.dumps(ios_output, indent=4))
