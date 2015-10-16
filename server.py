#import socket module
from socket import *
import sys

try:
	serverSocket = socket(AF_INET, SOCK_STREAM)
except Exception as ex:
	code, msg = ex.args
	print("Connection error. code: " + str(code) + " message: " + msg)

#Prepare a sever socket
#Fill in start
HOST = 'localhost'
PORT = 8000

try:
		serverSocket.bind((HOST, PORT))
except Exception as ex:
		print('Bind failed')
		sys.exit()

# Start listening
serverSocket.listen(10)
#Fill in end
while True:
		#Establish the connection
		print('Ready to serve...')
		connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
		try:
				message = connectionSocket.recv(1024).decode(encoding='utf-8')#Fill in start #Fill in end

				print('Connection received from ' + str(addr))
				filename = message.split(' ')[1]
				f = open(filename[1:]) 
				outputdata = f.readlines() #Fill in start #Fill in end
				#Send one HTTP header line into socket
				#Fill in start
				connectionSocket.send(b"HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n") 
				#Fill in end
				#Send the content of the requested file to the client
				for i in range(0, len(outputdata)):
						connectionSocket.send(bytes(outputdata[i], encoding="utf-8"))
				connectionSocket.close()
		except IOError:
				#Send response message for file not found
 		 		#Fill in start
				connectionSocket.send(b"HTTP/1.1 404 Not Found\r\nContent-Type: text/html;charset=UTF-8\r\n\r\n")
 				#Fill in end
				f = open('404.html')
				outputdata = f.readlines()
				
				for i in range(0, len(outputdata)):
						connectionSocket.send(bytes(outputdata[i], encoding="utf-8"))

				#Close client socket
 				#Fill in start
				connectionSocket.close()
 		 		#Fill in end 
serverSocket.close() 
