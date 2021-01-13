import telnetlib

host = "192.168.0.101"
port = 23

tn = telnetlib.Telnet(host, port)
tn.interact()

tn.close()
