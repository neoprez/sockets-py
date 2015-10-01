# handling errors in python socket programs

import socket #for sockets
import sys #for exit

try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as err:
	code, msg = inst.args
	print('Failed to create socket. Error code: ' + str(code) + ', Error message : ' + msg)
	sys.exit();

print('Socket Created')
