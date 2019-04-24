import socket
import subprocess
import sys

remoteServer    = socket.gethostname()
remoteServerIP  = socket.gethostbyname(remoteServer)
print("Host : ", remoteServerIP)
print("Please wait, this may take 10 to 20 minutes")
try:
    for port in range(1,1025):  
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0: #Zero means port is open
            print ("Port {} is Open".format(port))
        sock.close()

except KeyboardInterrupt:
    print("Keyboard Interrupt")
    sys.exit()
