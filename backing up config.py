import getpass
import telnetlib  # importing the telnet library

user = input("Enter your remote telnet username: ")
password = getpass.getpass()  # requesting for a password

f = open('myswitches') #opens a folder named myswitches from d NETAUTO container n assigning it 2 varaible f

for ip in f: #for each ip address found in the variable f
    ip = ip.strip() #strips any spaces found within ip address
    print('Getting running Config from ' + (ip))
    HOST = ip # each instance of ip address in d 'for loop' above is assigned to the varaible HOST
    Tel = telnetlib.Telnet(HOST)  # telnetting to the switch

    Tel.read_until(b"Username: ")  # runs the code until Username is displayed
    # write the user.variable to the network device
    Tel.write(user.encode('ascii') + b"\n")
    if password:
        Tel.read_until(b"Password: ") # runs the code until Password is displayed
        print('Please wait while we configure device')
        Tel.write(password.encode('ascii') + b"\n") # write the password.variable to the network device

    Tel.write(b"enable\n")
    Tel.write(b"cisco\n")
    Tel.write(b"terminal length 0\n")
    Tel.write(b"show run\n")
    Tel.write(b"exit\n")
    
    readoutput = Tel.read_all() #copies the running config into memory
    saveoutput = open('switch' + HOST, 'w') #creats a file switch + host(ip address) in a writeread format
    saveoutput.write(readoutput.decode('ascii')) #writes/paste the running config from the readoutput into the saveoutput varaible
    saveoutput.write('\n')
    saveoutput.close
    print('Backup Successful') 
