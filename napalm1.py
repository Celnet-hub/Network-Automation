import json
from napalm import get_network_driver
driver = get_network_driver('ios')
ios = driver(' 192.168.122.253','celestine','cisco')

ios.open() # opens my connection to the device

ios_output = ios.get_facts()
print (json.dumps(ios_output,indent = 4))

ios_output = ios.get_interfaces_counters()
print(json.dumps(ios_output, indent=4))
