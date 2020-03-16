import getpass
import telnetlib    #importing the telnet library 

HOST = "192.168.122.254" 
user = input("Enter your remote telnet username: ")
password = getpass.getpass()  #requesting for a password 

Tel = telnetlib.Telnet(HOST)  #telneting to the switch

Tel.read_until(b"Username: ")  #runs the code until Username is displayed 
Tel.write(user.encode('ascii') + b"\n") #write the user.variable to the network device
if password:
    Tel.read_until(b"Password: ") #runs the code until Password is displayed 
    Tel.write(password.encode('ascii') + b"\n")  #write the password.variable to the network device

Tel.write(b"enable\n")
Tel.write(b"cisco\n")
Tel.write(b"conf t\n")
Tel.write(b"int loop 0\n")
Tel.write(b"ip add 1.1.1.1 255.255.255\n")
Tel.write(b"int loop 1\n")
Tel.write(b"ip add 2.2.2.2 255.255.255\n")
Tel.write(b"int loop 2\n")
Tel.write(b"ip add 3.3.3.3 255.255.255\n")
Tel.write(b"router ospf 1\n")
Tel.write(b"network 0.0.0.0 255.255.255.255 area 0\n")
Tel.write(b"end\n")
Tel.write(b"wr\n")
Tel.write(b"exit\n")

print(Tel.read_all().decode('ascii')) 