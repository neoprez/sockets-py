# handling errors in python socket programs
import socket #for sockets
import sys #for exit

try:
	#create an AF_INET, STREAM socket (TCP)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except Exception as err:
	code, msg = inst.args
	print('Failed to create socket. Error code: ' + str(code) + ', Error message : ' + msg)
	sys.exit()

print('Socket Created')

host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname(host)
except Exception as err:
	#could not resolve
	print('Hostname could not be resolved. Exiting')
	sys.exit()

print('Ip address of ' + host + ' is ' + remote_ip)

#Connect to remote server
s.connect((remote_ip, port))

print('Socket Connected to ' + host + ' on ip ' + remote_ip)

#Send some data to remote server
# socket.sendall accepts byte string (str in Python 2.x, bytes in Python 3.x). In Python 3.x, you should use bytes literal
message = b"GET / HTTP/1.1\r\n\r\n"

try:
	#Set the whole string
	s.sendall(message)
except Exception as err:
	print('Send failed.')
	sys.exit()

print('Message send successfully')
