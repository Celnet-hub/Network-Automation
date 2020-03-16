import getpass
import telnetlib    #importing the telnet library 

HOST = "192.168.122.253" 
user = input("Enter your remote telnet username: ")
password = getpass.getpass()  #requesting for a password 

Tel = telnetlib.Telnet(HOST)  #telneting to the switch

Tel.read_until(b"Username: ")  #runs the code until Username is displayed 
Tel.write(user.encode('ascii') + b"\n") #write the user.variable to the network device
if password:
    Tel.read_until(b"Password: ") #runs the code until Password is displayed 
    print('Please wait while we connect device')
    Tel.write(password.encode('ascii') + b"\n")  #write the password.variable to the network device

Tel.write(b"enable\n")
Tel.write(b"cisco\n")
Tel.write(b"conf t\n")
Tel.write(b"vl 2\n")
Tel.write(b"name python_vlan2\n")
Tel.write(b"vl 3\n")
Tel.write(b"name python_vlan3\n")
Tel.write(b"vl 4\n")
Tel.write(b"name python_vlan4\n")
Tel.write(b"vl 5\n")
Tel.write(b"name python_vlan5\n")
Tel.write(b"end\n")
Tel.write(b"wr\n")
Tel.write(b"exit\n")

print(Tel.read_all().decode('ascii')) 