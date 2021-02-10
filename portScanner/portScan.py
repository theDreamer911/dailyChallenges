import socket
import subprocess
import sys
import platform
from datetime import datetime

if platform.system() == 'Windows':
    subprocess.call('cls', shell=True)
else:
    subprocess.call('clear', shell=True)


# input
remoteServer = input('Enter host ip address: ')
remoteServerIP = socket.gethostbyname(remoteServer)

# styling header
print('-' * 60)
print(f'Please wait, scanning on progress {remoteServerIP}')
print('-' * 60)

# Time started
t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print(f"Port {port}: Open")
        sock.close()

except KeyboardInterrupt:
    print("Ctrl+C pressed, Exiting")
    sys.exit()

except socket.gaierror:
    print("Hostname can't be resolved, Exiting")
    sys.exit()

except socket.error:
    print("Couldn't connect to the server, Exiting")
    sys.exit()

# Check time
t2 = datetime.now()

# Count different time
total = t2 - t1

print(f'Scanning Completed in: {total}')
