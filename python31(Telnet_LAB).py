import getpass
import telnetlib  # importing the telnet library

HOST = "192.168.122.254"
user = input("Enter your remote telnet username: ")

password = getpass.getpass()  # requesting for a password

if password == 'cisco':
   print('Connecting to R1 @ ' + HOST)
   try:
       Tel = telnetlib.Telnet(HOST)  # telneting to the switch
   except:
       print('Unable to establish remote connection... transport input maybe set to none....')
       exit()
elif password != 'cisco':
   print('Please input correct password....')
   password = getpass.getpass()  # requesting for a password
   if password != 'cisco':
      print('Limit reached... ')
   exit()


Tel.read_until(b"Username: ")  # runs the code until Username is displayed
# write the user.variable to the network device
Tel.write(user.encode('ascii') + b"\n")
if password:
    Tel.read_until(b"Password: ")  # runs the code until Password is displayed
    # write the password.variable to the network device
    Tel.write(password.encode('ascii') + b"\n")

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
