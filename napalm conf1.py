import json
from napalm import get_network_driver

driver = get_network_driver('ios')
deviceIP = ['192.168.122.253', '192.168.122.254']

for ip in deviceIP:
    print('Accessiing ' + ip)
    iosl2 = driver(ip, 'celestine', 'cisco')
    iosl2.open()
    iosl2.load_merge_candidate(filename = 'ACL1.cfg')
    iosl2.commit_config()
    iosl2.colse()
