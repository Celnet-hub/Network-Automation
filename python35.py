import getpass
import telnetlib  # importing the telnet library

HOST = "Local Host Device"
user = input("Enter your remote telnet username: ")
password = getpass.getpass()  # requesting for a password

f = open('myswitches')

for ip in f:
    ip = ip.strip()
    print('connecting to network device ' + (ip))
    HOST = ip
    Tel = telnetlib.Telnet(HOST)  # telneting to the switch

    Tel.read_until(b"Username: ")  # runs the code until Username is displayed
    # write the user.variable to the network device
    Tel.write(user.encode('ascii') + b"\n")
    if password:
        Tel.read_until(b"Password: ")  # runs the code until Password is displayed
        print('Please wait while we configure device')
        # write the password.variable to the network device
        Tel.write(password.encode('ascii') + b"\n")

    Tel.write(b"enable\n")
    Tel.write(b"cisco\n")
    Tel.write(b"conf t\n")
    for n in range(2, 11):
        Tel.write(b'vlan ' + str(n).encode('ascii') + b'\n')
        Tel.write(b'name Python_VLAN ' + str(n).encode('ascii') + b'\n')
    Tel.write(b"end\n")
    Tel.write(b"wr\n")
    Tel.write(b"exit\n")

    print(Tel.read_all().decode('ascii'))
