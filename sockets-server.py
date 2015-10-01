import socket
import sys

HOST = '' # Symbolic name meaning all available interfaces
PORT = 8888 #Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
	s.bind((HOST,PORT))
except Exception as err:
	code, msg = err.args
	print("Bind failed. Error code: " + str(code) + ' msg: ' + msg)
	sys.exit()

print('Socket bind complete')

s.listen(10)
print("Socket now listening")
