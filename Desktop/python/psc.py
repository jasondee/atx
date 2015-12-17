import sys
import socket
import subprocess

remoteServer = raw_input("Hostname: ")
remoteServerip = socket.gethostbyname(remoteServer)

print "Please Hold, this process could take 3 minutes."

for port in range(1,1025):
	sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	result = sock.connect_ex((remoteServerip,port))
	if result == 0:
		print "Port {}:\t Open".format(port)
	sock.close
