import socket
import sys
import threading

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

# Function for handling connections. This will be used to create threads
def clientthread(conn):
	#Sending message to connected client
	conn.send(b'Welcome to the server. Type something and hit enter\n')
	
	#Infinte loop so that the function do not terminate and do not end.
	while True:
		
		#Receiving from client
		data = conn.recv(1024)
		reply = b'Ok...' + data
		if not data:
			break

		conn.sendall(reply)

	#come out of loop
	conn.close()

# now keep talking with the client
while 1:
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	print('Connected with ' + addr[0] + ':' + str(addr[1]))
	
	#start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function
	threading.Thread(target=clientthread,args=(conn,)).start()
	#start_new_thread(clientthread, (conn,))

s.close()
